# coding=utf-8

import unittest
import openprovider


class ApiTestCase(unittest.TestCase):
    api = None

    def setUp(self):
        url = "https://api.cte.openprovider.eu"
        self.api = openprovider.OpenProvider('antagonistbv-test', 'antagonistbv', url=url)
