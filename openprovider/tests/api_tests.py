# coding=utf-8

try:  # Python 2.6 compatibility
    import unittest2 as unittest
except ImportError:
    import unittest

from betamax import Betamax
from functools import wraps
from openprovider.api import api_factory


def configure_betamax(api, **additional_apis):
    with Betamax.configure() as config:
        config.cassette_library_dir = 'openprovider/tests/fixtures/cassettes'
        config.match_requests_on = ['method', 'uri', 'body']

        def _set_api(api, template):
            for attr in ('username', 'password', 'password_hash'):
                value = getattr(api, attr, None)
                if value:
                    config.define_cassette_placeholder(template % attr.upper(), value)

        # Configure primary API
        config.define_cassette_placeholder('<URL>', api.url)
        _set_api(api, '<%s>')

        # Any additional APIs
        for name, api in additional_apis.items():
            template = '<' + name.upper() + '_%s>' if name else '<%s>'
            _set_api(api, template)


def betamaxed(original_function):

    @wraps(original_function)
    def new_function(instance, *args, **kwargs):
        with Betamax(instance.api.session).use_cassette(original_function.__name__):
            return original_function(instance, *args, **kwargs)

    return new_function


class ApiTestCase(unittest.TestCase):
    """Superclass for all API test cases. Sets up the self.api value."""

    api = None

    def setUp(self):
        self.api = api_factory('test')
        configure_betamax(self.api)
