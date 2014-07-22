# coding=utf-8

"""Contains tests both for the models system and for the models themselves."""

import unittest
from openprovider.models import Model, Name, Domain, Phone


class TestModels(unittest.TestCase):
    """Tests for the model system."""

    def test_construct_kwargs(self):
        """Tests construction of a Model by keyword arguments."""
        mod = Model(foo="foo", bar=Model(baz="baz"))
        self.assertEqual(mod.foo, "foo")
        self.assertEqual(mod.bar.baz, "baz")

    def test_case_alias(self):
        """Tests Model's case-aliasing magic."""
        mod = Model(spam_and_eggs="Spam, spam, glorious spam")
        self.assertTrue(mod.spam_and_eggs)

    def test_name_str(self):
        """Tests the Name model and its string conversion."""
        leo = Name(first_name="Leonardo", prefix="da", last_name="Vinci")
        self.assertEqual(str(leo), "Leonardo da Vinci")

    def test_domain_str(self):
        """Tests the Domain model and its string conversion."""
        dom = Domain(name="example", extension="com")
        self.assertEqual(str(dom), "example.com")

    def test_phone_str(self):
        """Tests the Phone model and its string conversion."""
        country = "+31"
        area = "026"
        subscr = "3557772"

        p = Phone(country_code=country, area_code=area, subscriber_number=subscr)
        self.assertEqual(str(p), "+31 026 3557772")
