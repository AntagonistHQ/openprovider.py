import pytest
import os

from openprovider.api import api_factory


def test_api_factory_no_env():
    with pytest.raises(KeyError) as excinfo:
        api_factory('myaccount')
    assert str(excinfo.value) == "'Missing openprovider username for account myaccount'"


def test_api_factory_with_env():
    os.environ['OPENPROVIDER_APIFACTORY_TEST_USERNAME'] = 'myusername'
    os.environ['OPENPROVIDER_APIFACTORY_TEST_PASSWORD'] = 'mypassword'

    api = api_factory('apifactory_test')

    assert api.username == 'myusername'
    assert api.password == 'mypassword'
