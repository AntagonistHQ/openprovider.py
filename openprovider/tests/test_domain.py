# coding=utf-8

import calendar

from betamax import Betamax

from datetime import datetime as dt

from openprovider.api import api_factory
from openprovider.exceptions import NoSuchElement
from openprovider.models import DomainDetails, RegistryDetails
from openprovider.tests import ApiTestCase, configure_betamax, betamaxed


class DomainTestCase(ApiTestCase):

    def test_transfer(self):
        try:
            secundary_api = api_factory('test_secundary')
            configure_betamax(self.api, second=secundary_api)
        except KeyError:
            self.skipTest("No secundary account configured")

        domain = 'ci-%d.com' % calendar.timegm(dt.now().timetuple())
        primary_handle = 'YN000088-NL'
        secundary_handle = 'YN000101-NL'

        # Register a domain at the primary account
        with Betamax(self.api.session).use_cassette('domain_transfer_create'):
            response = self.api.domain.create_domain_request(
                    domain, 1, primary_handle, primary_handle, primary_handle,
                    ns_group='dns-openprovider',
            )

        auth_code = str(response.auth_code)

        # Now transfer it to the second account
        with Betamax(secundary_api.session).use_cassette('domain_transfer_transfer'):
            response = secundary_api.domain.transfer_domain_request(
                    domain, 1, auth_code, secundary_handle, secundary_handle, secundary_handle,
                    ns_group='dns-openprovider',
            )
        self.assertEqual(response.status, 'ACT')

        # Should be gone at the first provider
        with Betamax(self.api.session).use_cassette('domain_transfer_retrieve_old_registry'):
            self.assertRaises(NoSuchElement, self.api.domain.retrieve_domain_request, domain)

        # And be there at the second
        with Betamax(secundary_api.session).use_cassette('domain_transfer_retrieve_new_registry'):
            self.assertFalse(secundary_api.domain.retrieve_domain_request(domain) is None)

        # Try to clean up
        try:
            with Betamax(secundary_api.session).use_cassette('domain_transfer_delete_domain'):
                secundary_api.delete_domain_request(domain)
        except:
            pass

    @betamaxed
    def test_domain_details_with_registry_details(self):
        # Hand modified to ensure registryDetails were in place
        del self.api.session.headers['Accept-Encoding']

        response = self.api.domain.retrieve_domain_request('antagonist.net', registry_details=True)

        self.assertFalse(response is None)
        self.assertTrue(isinstance(response, DomainDetails))
        self.assertTrue(isinstance(response.registry_details, RegistryDetails))
        self.assertTrue(len(response.registry_details.messages) > 0)
        self.assertTrue(isinstance(response.registry_details.messages[0].date, dt))
        self.assertTrue(isinstance(response.registry_details.messages[0].message, str))
