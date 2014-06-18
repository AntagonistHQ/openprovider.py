# coding=utf-8

import lxml
import lxml.objectify
import lxml.etree
import requests

from openprovider import response
from openprovider.modules import *
from openprovider.data.exception_map import from_code


class OpenProvider(object):
    username = None
    password = None
    URL = "https://api.openprovider.eu"

    def __init__(self, username, password):
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

        apiresponse = requests.post(self.URL, data=apirequest)
        tree = lxml.objectify.fromstring(apiresponse.content)

        if tree.reply.code == 0:
            return response.Response(tree)
        else:
            klass = from_code(tree.reply.code)
            raise klass(tree.reply.desc)

