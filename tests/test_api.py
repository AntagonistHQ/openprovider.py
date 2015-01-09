import os

try:  # Python 2.6 compatibility
    from unittest2 import TestCase
except ImportError:
    from unittest import TestCase

from openprovider.api import api_factory


class ApiFactoryTest(TestCase):
    def test_no_env(self):
        with self.assertRaises(KeyError) as cm:
            api_factory('myaccount')
        self.assertEqual(str(cm.exception), "'Missing openprovider username for account myaccount'")

    def test_with_env(self):
        os.environ['OPENPROVIDER_APIFACTORY_TEST_USERNAME'] = 'myusername'
        os.environ['OPENPROVIDER_APIFACTORY_TEST_PASSWORD'] = 'mypassword'

        api = api_factory('apifactory_test')

        self.assertEqual(api.username, 'myusername')
        self.assertEqual(api.password, 'mypassword')
