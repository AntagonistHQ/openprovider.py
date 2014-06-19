# coding=utf-8

import unittest
from openprovider.models import *


class TestModels(unittest.TestCase):
    def test_construct_kwargs(self):
        mod = Model(foo="foo", bar=Model(baz="baz"))
        self.assertEqual(mod.foo, "foo")
        self.assertEqual(mod.bar.baz, "baz")

    def test_name_str(self):
        leo = Name(firstName="Leonardo", prefix="da", lastName="Vinci")
        self.assertEqual(str(leo), "Leonardo da Vinci")

    def test_domain_str(self):
        dom = Domain(name="example", extension="com")
        self.assertEqual(str(dom), "example.com")

    def test_phone_str(self):
        p = Phone(countryCode="+31", areaCode="026", subscriberNumber="3557772")
        self.assertEqual(str(p), "+31 026 3557772")
