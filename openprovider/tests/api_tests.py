# coding=utf-8

import unittest
from openprovider.api import api_factory


class ApiTestCase(unittest.TestCase):
    """Superclass for all API test cases. Sets up the self.api value."""

    api = None

    def setUp(self):
        self.api = api_factory('test')
