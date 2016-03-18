from __future__ import absolute_import

import pytest
import uuid

from openprovider.api import api_factory
from openprovider.models import Nameserver
from .api_tests import configure_betamax


@pytest.fixture
def api():
    api = api_factory('test')
    configure_betamax(api)
    return api


@pytest.fixture
def domainname(sld=None, tld='nl'):
    """Generate a psuedorandom domain name."""
    if sld is None:
        sld = uuid.uuid4()
    return 'ci-%s.%s' % (sld, tld)


@pytest.fixture
def nameservers():
    """Return the name servers for example.com."""
    return [
        Nameserver(name='a.iana-servers.net', ip='199.43.132.53', ip6='2001:500:8c::53'),
        Nameserver(name='b.iana-servers.net', ip='199.43.133.53', ip6='2001:500:8d::53'),
    ]
