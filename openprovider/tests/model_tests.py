# coding=utf-8

import unittest
from openprovider.models import *


class ModelTests(unittest.TestCase):
    def test_construct_kwargs(self):
        mod = Model(foo="foo", bar=Model(baz="baz"))
        self.assertEqual(mod.foo, "foo")
        self.assertEqual(mod.bar.baz, "baz")
