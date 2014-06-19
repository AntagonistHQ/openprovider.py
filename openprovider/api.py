# coding=utf-8

import lxml
import lxml.objectify
import lxml.etree

from openprovider import response
from openprovider import anyhttp
from openprovider.modules import *
from openprovider.data.exception_map import from_code


class OpenProvider(object):
    username = None
    password = None

    http = None

    def __init__(self, username, password, url="https://api.openprovider.eu"):
        self.username = username
        self.password = password

        # Initialize and add all modules.
        self.customers = customer.CustomerModule().with_parent(self)
        self.domains = domain.DomainModule().with_parent(self)
        self.extensions = extension.ExtensionModule().with_parent(self)
        self.nameserver = nameserver.NameserverModule().with_parent(self)
        self.nsgroup = nsgroup.NSGroupModule().with_parent(self)
        self.ssl = ssl.SSLModule().with_parent(self)
        self.reseller = reseller.ResellerModule().with_parent(self)
        self.financial = financial.FinancialModule().with_parent(self)

        # Set up Requests session
        self.http = anyhttp.HttpClient.any(url)

    def request(self, tree, **kwargs):
        e = lxml.objectify.ElementMaker(annotate=False)

        apirequest = lxml.etree.tostring(
            e.openXML(
                e.credentials(
                    e.username(self.username),
                    e.password(self.password),
                ),
                tree
            ),

            encoding='utf-8',
            xml_declaration=True
        )

        apiresponse = self.http.post(apirequest)
        tree = lxml.objectify.fromstring(apiresponse)

        if tree.reply.code == 0:
            return response.Response(tree)
        else:
            klass = from_code(tree.reply.code)
            raise klass("{0} ({1})".format(tree.reply.desc, tree.reply.code))

