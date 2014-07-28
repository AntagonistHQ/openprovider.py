# coding=utf-8

from openprovider.modules import E, common
from openprovider.models import Reseller


class ResellerModule(common.Module):
    """Bindings to API methods in the reseller module."""

    def retrieve(self):
        """
        Retrieve contact information on ourselves.
        """
        response = self.request(E.retrieveResellerRequest())
        return Reseller(response.data)
