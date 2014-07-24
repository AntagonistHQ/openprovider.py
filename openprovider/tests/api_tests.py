# coding=utf-8

import unittest
import openprovider


class ApiTestCase(unittest.TestCase):
    """Superclass for all API test cases. Sets up the self.api value."""

    api = None

    def setUp(self):
        self.api = ApiTestCase.api_factory()

    @staticmethod
    def api_factory():
        username = 'antagonistbv-test'
        password = 'antagonistbv'
        url = "https://api.cte.openprovider.eu"
        return openprovider.OpenProvider(username, password, url=url)

