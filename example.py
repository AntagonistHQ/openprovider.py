# coding=utf-8

import openprovider

op = openprovider.OpenProvider("test", "test")
print(op.domains.check("this-is-a-test-214123214.info"))
