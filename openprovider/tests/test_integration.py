# coding=utf-8

"""
The test_integration module provides integration (black-box) tests for the
entire library.
"""

from openprovider import tests
from openprovider.data.sslcerts import CertTypes
from openprovider.exceptions import BadRequest
from openprovider.models import Reseller, Address

import textwrap


class TestDomains(tests.ApiTestCase):
    """Smoke tests for the domain module."""

    def test_domain_check_active(self):
        """Obviously taken domains should return 'active'."""
        self.assertEqual(self.api.domains.check("example.com"), "active")

    def test_domain_check_free(self):
        """Obviously free domain should return 'free'."""
        self.assertEqual(self.api.domains.check("oy6uT6caew3deej.com"), "free")

    def test_domain_check_invalid(self):
        """All kinds of invalid domains should raise a BadRequest."""
        self.assertRaises(BadRequest, self.api.domains.check, "a.invalid")
        self.assertRaises(BadRequest, self.api.domains.check, "a.com")

    def test_domain_check_many(self):
        """Test for checking multiple domains."""
        result = self.api.domains.check_many(["example.com", "example.net"])
        self.assertEqual(result,
                         {"example.com": "active", "example.net": "active"})


class TestExtensions(tests.ApiTestCase):
    """Smoke tests for the extensions module."""

    def test_search_extension(self):
        """Search should return something sensible."""
        r = self.api.extensions.search_extension(with_usage_count=True)
        self.assertTrue(r[0].usage_count is not None)

    def test_retrieve_extension(self):
        """Retrieve should return a proper Extension."""
        r = self.api.extensions.retrieve_extension("nl", with_description=True)
        self.assertTrue(r.description is not None)


class TestSSL(tests.ApiTestCase):
    """Smoke tests for the SSL module."""

    def test_ssl_search_product(self):
        """Test for the SSL product search method."""
        result = self.api.ssl.search_product()
        self.assertTrue(result[0].id)

    def test_ssl_retrieve_product(self):
        """Test for retrieving details on a single product."""
        res = self.api.ssl.retrieve_product(CertTypes.COMODO_EV_SSL.product_id)
        self.assertEqual(res.id, CertTypes.COMODO_EV_SSL.product_id)

    def test_ssl_order(self):
        """Test that orders a SSL certificate, then cancels it."""

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

        cert = CertTypes.COMODO_ESSENTIALSSL.product_id
        cust = "YN000088-NL"

        cname = "example.com"
        mail1 = "admin@example.com"
        mail2 = "administrator@example.com"

        decoded_csr = self.api.ssl.decode_csr(csr)
        self.assertEqual(cname, decoded_csr.subject.commonName)

        oid = self.api.ssl.create(cert, 1, csr, "linux", cust, mail1)

        self.assertTrue(cust,
                        self.api.ssl.retrieve_order(oid).organizationHandle)

        self.assertTrue(oid,
                        self.api.ssl.change_approver_email_address(oid, mail2))

        self.assertEqual(oid, self.api.ssl.resend_approver_email(oid))
        self.assertEqual(oid, self.api.ssl.cancel(oid))

    def test_ssl_approver_email(self):
        """Test for retrieving a list of allowed approver email addresses."""
        cert = CertTypes.COMODO_ESSENTIALSSL.product_id
        emails = self.api.ssl.retrieve_approver_email_list("example.com", cert)
        self.assertTrue("admin@example.com" in emails)


class TestReseller(tests.ApiTestCase):
    """Smoke tests for the reseller module."""
    def test_reseller_retrieve(self):
        r = self.api.reseller.retrieve()
        self.assertTrue(isinstance(r, Reseller))
        self.assertTrue(isinstance(r.address, Address))


class TestCustomer(tests.ApiTestCase):
    """Smoke tests for the customer module."""
    def test_customer_search(self):
        r = self.api.customers.search_customer()
        self.assertTrue(len(r) >= 1)

        r = self.api.customers.search_customer(email_pattern="doesntexist.com")
        self.assertTrue(len(r) == 0)
