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


from openprovider.modules import customer
from openprovider.modules import domain
from openprovider.modules import extension
from openprovider.modules import financial
from openprovider.modules import nameserver
from openprovider.modules import nsgroup
from openprovider.modules import reseller
from openprovider.modules import ssl
