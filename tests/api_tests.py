# coding=utf-8

from betamax import Betamax
from functools import wraps


def configure_betamax(api, **additional_apis):
    with Betamax.configure() as config:
        config.cassette_library_dir = 'tests/fixtures/cassettes'
        config.default_cassette_options['match_options'] = ['method', 'uri', 'body']

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
    def new_function(api, *args, **kwargs):
        with Betamax(api.session).use_cassette(original_function.__name__):
            return original_function(api, *args, **kwargs)

    return new_function
