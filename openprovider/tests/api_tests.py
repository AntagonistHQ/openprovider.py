# coding=utf-8

import unittest
import openprovider


class ApiTestCase(unittest.TestCase):
    api = None

    def setUp(self):
        self.api = openprovider.OpenProvider('test', 'test')
