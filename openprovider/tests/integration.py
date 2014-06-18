# coding=utf-8

import unittest
import openprovider


class IntegrationTest(unittest.TestCase):
    """
    A set of smoke tests that test the complete stack against the live API.
    """

    def setUp(self):
        self.api = openprovider.OpenProvider('test', 'test')

    def test_domain_active(self):
        self.assertEqual(self.api.domains.check("openprovider.eu"), "active")

    def test_domain_free(self):
        self.assertEqual(self.api.domains.check("oy6uT6caew3deej.com"), "free")
