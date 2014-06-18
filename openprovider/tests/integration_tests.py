# coding=utf-8

from openprovider import tests
from openprovider.exceptions import *


class IntegrationTest(tests.ApiTestCase):
    """
    A set of smoke tests that test the complete stack against the live API.
    """
    def test_domain_active(self):
        self.assertEqual(self.api.domains.check("openprovider.eu"), "active")

    def test_domain_free(self):
        self.assertEqual(self.api.domains.check("oy6uT6caew3deej.com"), "free")

    def test_domain_invalid(self):
        self.assertRaises(BadRequest, self.api.domains.check, "invalid.invalid")
