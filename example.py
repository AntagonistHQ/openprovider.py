# coding=utf-8

import openprovider

op = openprovider.OpenProvider("test", "test")
print(op.domains.check("test.com"))
