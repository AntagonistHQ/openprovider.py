# coding=utf-8

from openprovider.modules import E, common
from openprovider.models import Model


class EmailModule(common.Module):
    """Bindings to API methods in the email module."""

    def restart_customer_email_verification_request(self, email):
        request = E.restartCustomerEmailVerificationRequest(E.email(email))
        response = self.request(request)
        return response.data

    def search_customer_email_verification_request(self, email):
        request = E.searchCustomerEmailVerificationRequest(E.email(email))
        response = self.request(request)

        try:
            return [Model(item) for item in response.data.results.array.item]
        except AttributeError:
            return []

    def start_customer_email_verification_request(self, email):
        request = E.startCustomerEmailVerificationRequest(E.email(email))
        response = self.request(request)
        return response.data.id
