# coding=utf-8

"""
This is a simple REPL for experimenting with the openprovider.py API. An
instance of the OpenProvider class is available as 'op'. The openprovider module
has been imported for you.

Use the environment variables OPENPROVIDER_USERNAME, OPENPROVIDER_PASSWORD and OPENPROVIDER_URL to
change the username and password.
"""

from openprovider.api import api_factory
import openprovider  # NOQA
import textwrap
import os

os.environ.setdefault('OPENPROVIDER_USERNAME', 'test')
os.environ.setdefault('OPENPROVIDER_PASSWORD', 'test')


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

op = api_factory()

print(textwrap.dedent(__doc__).strip())
print("")
print("Address:  %s" % op.url)
print("Username: %s" % op.username)

# Clean up the environment
del api_factory
del textwrap
del os

repl()
