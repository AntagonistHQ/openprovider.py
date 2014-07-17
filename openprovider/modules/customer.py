# coding=utf-8

from openprovider.modules import common
from openprovider.models import Customer


class CustomerModule(common.Module):
    """Bindings to API methods in the customer module."""

    def search_customer(self, limit=100, offset=0, **kw):
        """Search the list of customers."""

        e = self.e
        response = self.request(e.searchCustomerRequest(
            e.limit(limit),
            e.offset(offset),
            e.emailPattern(kw.get('email_pattern', '')),
            e.lastNamePattern(kw.get('last_name_pattern', '')),
            e.companyNamePattern(kw.get('company_name_pattern', '')),
            e.withAdditionalData(int(kw.get('with_additional_data', 0)))
        ))

        return response.as_models(Customer)

    def retrieve_customer(self, handle, **kw):
        """Retrieve information of an existing customer."""

        e = self.e
        response = self.request(e.retrieveCustomerRequest(
            e.handle(handle),
            e.withAdditionalData(int(kw.get('with')))
        ))

        return response.as_model(Customer)
