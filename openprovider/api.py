# coding=utf-8

from modules import *


class OpenProvider(object):
    username = None
    password = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.customers = customer.CustomerModule().with_parent(self)
        self.domains = domain.DomainModule().with_parent(self)
        self.extensions = extension.ExtensionModule().with_parent(self)
        self.nameserver = nameserver.NameserverModule().with_parent(self)
        self.nsgroup = nsgroup.NSGroupModule().with_parent(self)
        self.ssl = ssl.SSLModule().with_parent(self)
        self.reseller = reseller.ResellerModule().with_parent(self)
        self.financial = financial.FinancialModule().with_parent(self)

