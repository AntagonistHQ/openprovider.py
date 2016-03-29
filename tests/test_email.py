import pytest
import uuid

from openprovider.exceptions import ValidationError

from . import betamaxed

# These tests are a bit flawed in that we expect some things to exist or not exist, but since
# it's betamaxed we can probably get away with it for a long time


@betamaxed
def test_seach_non_existing(api):
    email = 'nonexisting@example.org'
    results = api.email.search_customer_email_verification_request(email)
    assert results == []


@betamaxed
def test_seach_existing(api):
    email = 'test@example.org'
    results = api.email.search_customer_email_verification_request(email)
    assert len(results) == 1

    result = results[0]
    assert result.name == email
    assert hasattr(result, 'id')
    assert hasattr(result, 'status')


@betamaxed
def test_start_verification(api):
    email = '%s@example.org' % uuid.uuid4()
    results = api.email.start_customer_email_verification_request(email)
    assert results is not None


@betamaxed
def test_restart_non_existing_verification(api):
    email = '%s@example.org' % uuid.uuid4()
    with pytest.raises(ValidationError) as excinfo:
        api.email.restart_customer_email_verification_request(email)
    assert excinfo.value.code == 1203


@betamaxed
def test_restart_existing_verification(api):
    email = 'demo@example.org'
    result = api.email.restart_customer_email_verification_request(email)
    assert result is not None
