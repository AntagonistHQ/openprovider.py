# coding=utf-8

import unittest
import openprovider


class ApiTestCase(unittest.TestCase):
    api = None

    def setUp(self):
        username = 'antagonistbv-test'
        password = 'antagonistbv'
        url = "https://api.cte.openprovider.eu"
        self.api = openprovider.OpenProvider(username, password, url=url)
