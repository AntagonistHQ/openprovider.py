# coding=utf-8

from openprovider.modules import common
from openprovider.models import SSLProduct, SSLOrder

import textwrap


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

    def search_order(self, limit=100, offset=0, **kwargs):
        e = self.e
        response = self.request(e.searchOrderSslCertRequest(
            e.limit(limit),
            e.offset(offset)
        ))
        return [SSLOrder(o) for o in response.data.results.array[0].item]

    def retrieve_order(self, order_id):
        response = self.request(self.e.retrieveOrderSslCertRequest(self.e.id(order_id)))
        return SSLOrder(response.data)

    def create(self, product_id, period, csr, software_id, organization_handle, approver_email, **kwargs):
        e = self.e
        response = self.request(e.createSslCertRequest(
            e.productId(product_id),
            e.period(period),
            e.csr(csr),
            e.softwareId(software_id),
            e.organizationHandle(organization_handle),
            e.approverEmail(approver_email),
        ))
        return int(response.data.id)

    def reissue(self):
        pass

    def cancel(self, order_id):
        response = self.request(self.e.cancelSslCertRequest(self.e.id(order_id)))
        return int(response.data.id)

    def retrieve_approver_email_list(self, domain, product_id):
        response = self.request(self.e.retrieveApproverEmailListSslCertRequest(
            self.e.domain(domain),
            self.e.productId(product_id)
        ))
        return [str(i) for i in response.data.array[0].item]

    def resend_approver_email(self, order_id):
        response = self.request(self.e.resendApproverEmailSslCertRequest(self.e.id(order_id)))
        return int(response.data.id)

    def change_approver_email_address(self, order_id, approver_email):
        response = self.request(self.e.changeApproverEmailAddressSslCertRequest(
            self.e.id(order_id),
            self.e.approverEmail(approver_email)
        ))
        return int(response.data.id)

    def decode_csr(self, csr):
        return self.request(self.e.decodeCsrSslCertRequest(self.e.csr(csr))).data
