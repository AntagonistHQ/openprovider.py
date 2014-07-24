# coding=utf-8

"""
This is a simple REPL for experimenting with the openprovider.py API. An
instance of the OpenProvider class is available as 'op'. The openprovider module
has been imported for you.
"""

import textwrap
import openprovider
import openprovider.tests
import openprovider.data

try:
    # Try to use IPython...
    from IPython import embed

    def repl():
        embed(banner1="")
except ImportError:
    # But if that fails, fall back to normal Python.
    import code

    def repl():
        code.interact(banner="", local=globals())


op = openprovider.tests.ApiTestCase.api_factory()
print(textwrap.dedent(__doc__).strip())
print("")
print("Address:  %s" % op.url)
print("Username: %s" % op.username)
repl()
