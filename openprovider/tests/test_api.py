import os

from unittest import TestCase

from openprovider.api import api_factory


class ApiFactoryTest(TestCase):
    def test_no_env(self):
        # Python 2.6 has no assertRaises that can act as context manager
        try:
            api_factory('myaccount')
        except KeyError as e:
            self.assertEqual(str(e), "'Missing openprovider username for account myaccount'")
        else:
            self.fail('Expected KeyError to be raised')

    def test_with_env(self):
        os.environ['OPENPROVIDER_APIFACTORY_TEST_USERNAME'] = 'myusername'
        os.environ['OPENPROVIDER_APIFACTORY_TEST_PASSWORD'] = 'mypassword'

        api = api_factory('apifactory_test')

        self.assertEqual(api.username, 'myusername')
        self.assertEqual(api.password, 'mypassword')
