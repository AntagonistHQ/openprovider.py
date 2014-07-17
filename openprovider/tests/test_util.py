# coding=utf-8

"""Contains tests for the utilities module."""

import unittest
from openprovider.util import *


class TestUtil(unittest.TestCase):
    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("name"), "name")
        self.assertEqual(camel_to_snake("companyName"), "company_name")
        self.assertEqual(camel_to_snake("spamAndEggs"), "spam_and_eggs")

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel("name"), "name")
        self.assertEqual(snake_to_camel("company_name"), "companyName")
        self.assertEqual(snake_to_camel("spam_and_eggs"), "spamAndEggs")
