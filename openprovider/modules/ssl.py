# coding=utf-8

from openprovider.modules import common
from openprovider.models import SSLProduct


class SSLModule(common.Module):
    def search_product(self, limit=100, offset=0, **kwargs):
        e = self.e
        response = self.request(e.searchProductSslCertRequest(
            e.limit(limit),
            e.offset(offset),
            e.withPrice(int(kwargs.get('with_price', 0))),
            e.withSupportedSoftware(int(kwargs.get('with_supported_software', 0))),
            e.withDescription(int(kwargs.get('with_description', 0)))
        ))
        return [SSLProduct(p) for p in response.data.results.array[0].item]

    def retrieve_product(self, product_id):
        response = self.request(self.e.retrieveProductSslCertRequest(self.e.id(product_id)))
        return SSLProduct(response.data)

    def search_order(self):
        pass

    def retrieve_order(self):
        pass

    def create(self):
        pass

    def reissue(self):
        pass

    def cancel(self):
        pass

    def retrieve_approver_email_list(self):
        pass

    def resend_approver_email(self):
        pass

    def change_approver_email_address(self):
        pass

    def decode_csr(self):
        pass
