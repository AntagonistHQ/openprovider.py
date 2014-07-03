# coding=utf-8

from openprovider import tests
from openprovider.data.sslcerts import CertType
from openprovider.exceptions import *
from openprovider.models import *

import textwrap


class TestIntegration(tests.ApiTestCase):
    """
    A set of smoke tests that test the complete stack against the live API.
    """
    def test_domain_check_active(self):
        self.assertEqual(self.api.domains.check("example.com"), "active")

    def test_domain_check_free(self):
        self.assertEqual(self.api.domains.check("oy6uT6caew3deej.com"), "free")

    def test_domain_check_invalid(self):
        self.assertRaises(BadRequest, self.api.domains.check, "invalid.invalid")

    def test_domain_check_short(self):
        self.assertRaises(BadRequest, self.api.domains.check, "a.com")

    def test_domain_check_many(self):
        r = self.api.domains.check_many(["example.com", "example.net"])
        self.assertEqual(r, {"example.com": "active", "example.net": "active"})

    def test_ssl_search_product(self):
        r = self.api.ssl.search_product()
        self.assertTrue(r[0].id)

    def test_ssl_retrieve_product(self):
        r = self.api.ssl.retrieve_product(CertType.COMODO_EV_SSL)
        self.assertEqual(r.id, CertType.COMODO_EV_SSL)

    def test_ssl_order(self):
        csr = textwrap.dedent("""
        -----BEGIN CERTIFICATE REQUEST-----
        MIICzjCCAbYCAQAwgYgxCzAJBgNVBAYTAk5MMRMwEQYDVQQIDApPdmVyaWpzc2Vs
        MREwDwYDVQQHDAhFbnNjaGVkZTEYMBYGA1UECgwPQW50YWdvbmlzdCBCLlYuMSEw
        HwYDVQQLDBhPUEVOUFJPVklERVIgUFkgVEVTVCBDU1IxFDASBgNVBAMMC2V4YW1w
        bGUuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7WvbK/VDTxc/
        9DFkYreQNZo6j+0TrFFX1kqopS/COkkTaNY4xl7B/bq/CBS34nfjRT8x05RhyP2F
        mrNf6fZzl+8boQwJ4eVIDMjTNNecAsKrDTlZqwtvauPPEZ0pV7v6fxO+QOMn1uJq
        ZV7F+vdZ0IUihFUNwQoh9RaIoGtkaAiv1fgH/nrUuci/A9PqH2IBPRf9cCiIt1eK
        WCMXvWFzxkTATPVO35GByjN1GyMgRwTVrP53MKGAUOvbI4awS5x/ByKgigFhfLwr
        M86SSz1ZejlwZ7WqXFgPardMXOYt63ybKASanUTEUAgaEeK/9eL/sKQvEB0tBHbK
        e4uEksNsxwIDAQABoAAwDQYJKoZIhvcNAQELBQADggEBANlOjT4ddIgf9Zg1kR6p
        zbSfwuKLjS/w5RrnT5HliSTRUT/N8tNd2hRiukPqayJGhxtUIvyPdJTYUumIOnhu
        9ZZJcQJQDr5mvhP9hWn4/4yxOuZRd9q7DeoPSDRTkz7MuygoXQGt0ehOMcZBsfUC
        Uqx6ReCDz9PqgCa75XPL041SVot0RVswiiV54JRN0/cKzaItvtvinf0bPpPA1IWX
        qYm2QyYYJ8ayAsIw64YukRSOXp+escQ4rLfR1Un+QvgJM05x47jX8JivO3utexca
        cDJkVtg8DtoP1O1iF+xhNcHeWXUNO+PWHS9jIjL2Ofb78LjMpBjnB7C1L8rYxxg8
        cXU=
        -----END CERTIFICATE REQUEST-----
        """).strip()

        cert = CertType.COMODO_ESSENTIALSSL
        cust = "YN000088-NL"

        cn = "example.com"
        e1 = "admin@example.com"
        e2 = "administrator@example.com"

        self.assertEqual(cn, self.api.ssl.decode_csr(csr).subject.commonName)

        order = self.api.ssl.create(cert, 1, csr, "linux", cust, e1)

        self.assertTrue(cust,
                        self.api.ssl.retrieve_order(order).organizationHandle)
        self.assertTrue(order,
                        self.api.ssl.change_approver_email_address(order, e2))

        self.assertEqual(order, self.api.ssl.resend_approver_email(order))
        self.assertEqual(order, self.api.ssl.cancel(order))

    def test_ssl_approver_email(self):
        cert = CertType.COMODO_ESSENTIALSSL
        emails = self.api.ssl.retrieve_approver_email_list("example.com", cert)
        self.assertTrue("admin@example.com" in emails)

    def test_reseller_retrieve(self):
        r = self.api.reseller.retrieve()
        self.assertTrue(isinstance(r, Reseller))
        self.assertTrue(isinstance(r.address, Address))
