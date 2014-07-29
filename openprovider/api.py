# coding=utf-8

"""
Entry point for the OpenProvider API.
"""

import lxml
import lxml.objectify
import lxml.etree

from openprovider.anyhttp import AnyHttpClient
from openprovider.data.exception_map import from_code
from openprovider.modules import E, MODULE_MAPPING
from openprovider.response import Response


def _get_module_name(module):
    """
    Return the module name.

    >>> from openprovider.modules import CustomerModule
    >>> _get_module_name(CustomerModule)
    'customer'

    >>> _get_module_name(OpenProvider)
    'openprovider'
    """
    name = module.__name__[:-6] if module.__name__.endswith('Module') else module.__name__
    return name.lower()


class OpenProvider(object):
    """A connection to the OpenProvider API."""

    def __init__(self, username, password, url="https://api.openprovider.eu"):
        """Initializes the connection with the given username and password."""
        self.username = username
        self.password = password
        self.url = url

        # Initialize and add all modules.
        for old_name, module in MODULE_MAPPING.items():
            name = _get_module_name(module)
            instance = module(self)
            setattr(self, name, instance)
            if old_name != name:
                setattr(self, old_name, instance)

        # Set up API client
        self.http = AnyHttpClient(url)

    def request(self, tree, **kwargs):
        """
        Construct a new request with the given tree as its contents, then ship
        it to the OpenProvider API.
        """

        apirequest = lxml.etree.tostring(
            E.openXML(
                E.credentials(
                    E.username(self.username),
                    E.password(self.password),
                ),
                tree
            ),

            method='c14n'
        )

        apiresponse = self.http.post(apirequest)
        tree = lxml.objectify.fromstring(apiresponse)

        if tree.reply.code == 0:
            return Response(tree)
        else:
            klass = from_code(tree.reply.code)
            desc = tree.reply.desc
            code = tree.reply.code
            data = tree.reply.data
            raise klass("{0} ({1}) {2}".format(desc, code, data))
