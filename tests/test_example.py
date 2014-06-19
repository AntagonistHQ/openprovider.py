# coding=utf-8

from betamax import Betamax
from openprovider import OpenProvider


with Betamax.configure() as config:
    config.cassette_library_dir = "tests/fixtures/cassettes"


def get_provider():
    return OpenProvider("test", "test")


def test_check_free():
    provider = get_provider()
    with Betamax(provider.session) as vcr:
        vcr.use_cassette("domain_free")
        assert provider.domains.check("this-is-a-test-214123214.info") == "free"


def test_check_taken():
    provider = get_provider()
    with Betamax(provider.session) as vcr:
        vcr.use_cassette("domain_taken")
        assert provider.domains.check("antagonist.nl") == "active"
