# coding=utf-8

import calendar
import pytest

from betamax import Betamax

from datetime import datetime as dt

from openprovider.api import api_factory
from openprovider.exceptions import BadRequest, NoSuchElement
from openprovider.models import DomainDetails, RegistryDetails
from . import configure_betamax, betamaxed


def test_transfer(api):
    try:
        secundary_api = api_factory('test_secundary')
        configure_betamax(api, second=secundary_api)
    except KeyError:
        pytest.skip("No secundary account configured")

    domain = 'ci-%d.com' % calendar.timegm(dt.now().timetuple())
    primary_handle = 'YN000088-NL'
    secundary_handle = 'YN000101-NL'

    # Register a domain at the primary account
    with Betamax(api.session).use_cassette('domain_transfer_create'):
        response = api.domain.create_domain_request(
                domain, 1, primary_handle, primary_handle, primary_handle,
                ns_group='dns-openprovider',
        )

    auth_code = str(response.auth_code)

    # Now transfer it to the second account
    with Betamax(secundary_api.session).use_cassette('domain_transfer_transfer'):
        response = secundary_api.domain.transfer_domain_request(
                domain, 1, auth_code, secundary_handle, secundary_handle, secundary_handle,
                ns_group='dns-openprovider',
        )
    assert response.status == 'ACT'

    # Should be gone at the first provider
    with Betamax(api.session).use_cassette('domain_transfer_retrieve_old_registry'):
        with pytest.raises(NoSuchElement):
            api.domain.retrieve_domain_request(domain)

    # And be there at the second
    with Betamax(secundary_api.session).use_cassette('domain_transfer_retrieve_new_registry'):
        secundary_api.domain.retrieve_domain_request(domain) is not None

    # Try to clean up
    try:
        with Betamax(secundary_api.session).use_cassette('domain_transfer_delete_domain'):
            secundary_api.delete_domain_request(domain)
    except:
        pass


@betamaxed
def test_domain_details_with_registry_details(api):
    # Hand modified to ensure registryDetails were in place
    del api.session.headers['Accept-Encoding']

    response = api.domain.retrieve_domain_request('antagonist.net', registry_details=True)

    assert response is not None
    assert isinstance(response, DomainDetails)
    assert isinstance(response.registry_details, RegistryDetails)
    assert len(response.registry_details.messages) > 0
    assert isinstance(response.registry_details.messages[0].date, dt)
    assert isinstance(response.registry_details.messages[0].message, str)


@betamaxed
def test_domain_check_active(api):
    """Obviously taken domains should return 'active'."""
    assert api.domains.check("example.com") == "active"


@betamaxed
def test_domain_check_free(api):
    """Obviously free domain should return 'free'."""
    assert api.domains.check("oy6uT6caew3deej.com") == "free"


@betamaxed
def test_domain_check_invalid_tld(api):
    """Domains with an invalid TLD should raise a BadRequest."""
    with pytest.raises(BadRequest):
        api.domains.check("a.com")


@betamaxed
def test_domain_check_invalid_sld(api):
    """Domains with an invalid SLD should raise a BadRequest."""
    with pytest.raises(BadRequest):
        api.domains.check("a.com")


@betamaxed
def test_domain_check_many(api):
    """Test for checking multiple domains."""
    result = api.domains.check_many(["example.com", "example.net"])
    assert result == {"example.com": "active", "example.net": "active"}


@betamaxed
def test_domain_search_empty(api):
    """Searching for example.com should return nothing."""
    result = api.domains.search_domain_request(domain_name_pattern="example.com")
    assert result == []


def test_domain_order(api, domainname, nameservers):
    """Test that creates a domain name, then deletes it."""
    cust = "YN000088-NL"

    with Betamax(api.session).use_cassette('test_domain_order_create'):
        api.domains.create_domain_request(
                domain=domainname,
                period=1,
                owner_handle=cust,
                admin_handle=cust,
                tech_handle=cust,
                name_servers=nameservers,
        )

    with Betamax(api.session).use_cassette('test_domain_order_modify'):
        api.domains.modify_domain_request(domainname, comments="Test")

    with Betamax(api.session).use_cassette('test_domain_order_retrieve'):
        result = api.domains.retrieve_domain_request(domainname)
        assert result.comments == "Test"
        assert result.owner_handle == cust
        assert result.admin_handle == cust
        assert result.tech_handle == cust

    with Betamax(api.session).use_cassette('test_domain_order_delete'):
        api.domains.delete_domain_request(domainname)

    with Betamax(api.session).use_cassette('test_domain_order_post'):
        result = api.domains.search_domain_request(domain_name_pattern=domainname)
        assert result == []


@betamaxed
def test_price_domain_default(api):
    dname = 'example.nl'

    result = api.domains.retrieve_price_domain_request(dname)

    assert result.is_premium is not None
    assert result.price is not None

    assert result.price.product is not None
    assert result.price.product.price is not None
    assert result.price.product.currency == 'EUR'

    assert result.price.reseller is not None
    assert result.price.reseller.price is not None
    assert result.price.reseller.currency is not None


@betamaxed
def test_price_domain_with_operation(api):
    dname = 'example.com'

    result = api.domains.retrieve_price_domain_request(dname, 'restore')

    assert result.is_premium is not None
    assert result.price is not None

    assert result.price.product is not None
    assert result.price.product.price is not None
    assert result.price.product.currency == 'USD'

    assert result.price.reseller is not None
    assert result.price.reseller.price is not None
    assert result.price.reseller.currency is not None
