from openprovider.models import Reseller, Address

from . import betamaxed


@betamaxed
def test_reseller_retrieve(api):
    r = api.reseller.retrieve()
    assert isinstance(r, Reseller)
    assert isinstance(r.address, Address)
