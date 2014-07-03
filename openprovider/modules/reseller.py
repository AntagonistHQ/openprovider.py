# coding=utf-8

from openprovider.modules import common
from openprovider.models import Reseller


class ResellerModule(common.Module):
    """Bindings to API methods in the reseller module."""

    def retrieve(self):
        """
        Retrieve contact information on ourselves.
        """
        response = self.request(self.e.retrieveResellerRequest())
        return Reseller(response.data)
