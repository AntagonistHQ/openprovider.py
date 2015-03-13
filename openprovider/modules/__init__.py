# coding=utf-8

import lxml

E = lxml.objectify.ElementMaker(annotate=False)


def OE(element, value, transform=lambda x: x):
    """
    Create an Optional Element.

    Returns an Element as ElementMaker would, unless value is None. Optionally the value can be
    transformed through a function.

    >>> OE('elem', None)
    None

    >>> lxml.etree.tostring(OE('elem', 'value'))
    <elem>value</elem>

    >>> lxml.etree.tostring(OE('elem', True, int))
    <elem>1</elem>
    """
    return E(element, transform(value)) if value is not None else None


from openprovider.modules.customer import CustomerModule
from openprovider.modules.domain import DomainModule
from openprovider.modules.email import EmailModule
from openprovider.modules.extension import ExtensionModule
from openprovider.modules.financial import FinancialModule
from openprovider.modules.nameserver import NameserverModule
from openprovider.modules.nsgroup import NSGroupModule
from openprovider.modules.reseller import ResellerModule
from openprovider.modules.ssl import SSLModule


MODULE_MAPPING = {
        'customers': CustomerModule,
        'domains': DomainModule,
        'email': EmailModule,
        'extensions': ExtensionModule,
        'financial': FinancialModule,
        'nameserver': NameserverModule,
        'nsgroup': NSGroupModule,
        'reseller': ResellerModule,
        'ssl': SSLModule,
}
