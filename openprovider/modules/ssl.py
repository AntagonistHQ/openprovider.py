# coding=utf-8

from openprovider.modules import E, common
from openprovider.models import SSLProduct, SSLOrder


class SSLModule(common.Module):
    """Bindings to API methods in the SSL module."""

    def search_product(self, limit=100, offset=0, **kw):
        """Search the list of available products."""

        response = self.request(E.searchProductSslCertRequest(
            E.limit(limit),
            E.offset(offset),
            E.withPrice(int(kw.get('with_price', 0))),
            E.withSupportedSoftware(int(kw.get('with_supported_software', 0))),
            E.withDescription(int(kw.get('with_description', 0)))
        ))
        return response.as_models(SSLProduct)

    def retrieve_product(self, product_id):
        """Retrieve details on a single product."""

        response = self.request(E.retrieveProductSslCertRequest(
            E.id(product_id)
        ))

        return response.as_model(SSLProduct)

    def search_order(self, limit=100, offset=0, **kwargs):
        """Search all SSL certificate orders."""

        response = self.request(E.searchOrderSslCertRequest(
            E.limit(limit),
            E.offset(offset)
        ))

        return response.as_models(SSLOrder)

    def retrieve_order(self, order_id):
        """Retrieve details on a single order."""

        response = self.request(E.retrieveOrderSslCertRequest(
            E.id(order_id)
        ))

        return response.as_model(SSLOrder)

    def create(self, product_id, period, csr, software_id, organization_handle,
               approver_email, **kwargs):
        """Order a new SSL certificate."""

        response = self.request(E.createSslCertRequest(
            E.productId(product_id),
            E.period(period),
            E.csr(csr),
            E.softwareId(software_id),
            E.organizationHandle(organization_handle),
            E.approverEmail(approver_email),
        ))

        return int(response.data.id)

    def reissue(self, order_id, csr, software_id, organization_handle, approver_email):
        """Reissue an SSL certificate order"""

        response = self.request(E.reissueSslCertRequest(
            E.id(order_id),
            E.csr(csr),
            E.softwareId(software_id),
            E.organizationHandle(organization_handle),
            E.approverEmail(approver_email),
        ))

        return int(response.data.id)

    def cancel(self, order_id):
        """Cancel an ordered SSL certificate."""

        response = self.request(E.cancelSslCertRequest(
            E.id(order_id)
        ))

        return int(response.data.id)

    def retrieve_approver_email_list(self, domain, product_id):
        """Retrieve the list of allowed approver email addresses."""

        response = self.request(E.retrieveApproverEmailListSslCertRequest(
            E.domain(domain),
            E.productId(product_id)
        ))

        return [str(i) for i in response.data.array[0].item]

    def resend_approver_email(self, order_id):
        """Resend the activation email to the approver."""

        response = self.request(E.resendApproverEmailSslCertRequest(
            E.id(order_id)
        ))

        return int(response.data.id)

    def change_approver_email_address(self, order_id, approver_email):
        """Change the approver email address for an ordered SSL certificate."""

        response = self.request(
            E.changeApproverEmailAddressSslCertRequest(
                E.id(order_id),
                E.approverEmail(approver_email)
            )
        )

        return int(response.data.id)

    def decode_csr(self, csr):
        """Decode a CSR and return its data."""

        response = self.request(E.decodeCsrSslCertRequest(
            E.csr(csr)
        ))

        return response.data
