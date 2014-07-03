# coding=utf-8

from openprovider import tests
from openprovider.data.sslcerts import CertType
from openprovider.exceptions import *
from openprovider.models import *


class TestIntegration(tests.ApiTestCase):
    """
    A set of smoke tests that test the complete stack against the live API.
    """
    def test_domain_check_active(self):
        self.assertEqual(self.api.domains.check("example.com"), "active")

    def test_domain_check_free(self):
        self.assertEqual(self.api.domains.check("oy6uT6caew3deej.com"), "free")

    def test_domain_check_invalid(self):
        self.assertRaises(BadRequest, self.api.domains.check, "invalid.invalid")

    def test_domain_check_short(self):
        self.assertRaises(BadRequest, self.api.domains.check, "a.com")

    def test_domain_check_many(self):
        r = self.api.domains.check_many(["example.com", "example.net"])
        self.assertEqual(r, {"example.com": "active", "example.net": "active"})

    def test_ssl_search_product(self):
        r = self.api.ssl.search_product()
        self.assertTrue(r[0].id)

    def test_ssl_retrieve_product(self):
        r = self.api.ssl.retrieve_product(CertType.COMODO_EV_SSL)
        self.assertEqual(r.id, CertType.COMODO_EV_SSL)

    def test_reseller_retrieve(self):
        r = self.api.reseller.retrieve()
        self.assertTrue(isinstance(r, Reseller))
        self.assertTrue(isinstance(r.address, Address))
