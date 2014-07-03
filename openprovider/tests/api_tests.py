# coding=utf-8

import unittest
import openprovider


class ApiTestCase(unittest.TestCase):
    """Superclass for all API test cases. Sets up the self.api value."""

    api = None

    def setUp(self):
        username = 'antagonistbv-test'
        password = 'antagonistbv'
        url = "https://api.cte.openprovider.eu"
        self.api = openprovider.OpenProvider(username, password, url=url)
