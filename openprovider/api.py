# coding=utf-8

"""
Entry point for the OpenProvider API.
"""

import lxml
import lxml.objectify
import lxml.etree

from openprovider import response
from openprovider import anyhttp
from openprovider.modules import E, customer, domain, extension, financial, \
    nameserver, nsgroup, reseller, ssl
from openprovider.data.exception_map import from_code


class OpenProvider(object):
    """A connection to the OpenProvider API."""

    def __init__(self, username, password, url="https://api.openprovider.eu"):
        """Initializes the connection with the given username and password."""
        self.username = username
        self.password = password
        self.url = url

        # Initialize and add all modules.
        self.customers = customer.CustomerModule(self)
        self.domains = domain.DomainModule(self)
        self.extensions = extension.ExtensionModule(self)
        self.nameserver = nameserver.NameserverModule(self)
        self.nsgroup = nsgroup.NSGroupModule(self)
        self.ssl = ssl.SSLModule(self)
        self.reseller = reseller.ResellerModule(self)
        self.financial = financial.FinancialModule(self)

        # Set up Requests session
        self.http = anyhttp.HttpClient.any(url)

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
            return response.Response(tree)
        else:
            klass = from_code(tree.reply.code)
            desc = tree.reply.desc
            code = tree.reply.code
            data = tree.reply.data
            raise klass("{0} ({1}) {2}".format(desc, code, data))
