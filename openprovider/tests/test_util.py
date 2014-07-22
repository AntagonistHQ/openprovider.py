# coding=utf-8

"""Contains tests for the utilities module."""

import unittest
from openprovider.util import *


class CamelToSnakeTest(unittest.TestCase):
    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("name"), "name")
        self.assertEqual(camel_to_snake("companyName"), "company_name")
        self.assertEqual(camel_to_snake("spamAndEggs"), "spam_and_eggs")

    def test_snake_camel_snake(self):
        self.assertEqual(camel_to_snake(snake_to_camel("country_code")), "country_code")


class SnakeToCamelTest(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel("name"), "name")
        self.assertEqual(snake_to_camel("company_name"), "companyName")
        self.assertEqual(snake_to_camel("spam_and_eggs"), "spamAndEggs")

    def test_camel_snake_camel(self):
        self.assertEqual(snake_to_camel(camel_to_snake("countryCode")), "countryCode")

    def test_camel_case_as_input(self):
        # This may not be what the user wants, but it is what it is
        self.assertEqual(snake_to_camel("countryCode"), "countrycode")
