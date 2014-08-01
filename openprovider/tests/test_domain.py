# coding=utf-8

import calendar

from datetime import datetime as dt

from openprovider.api import api_factory
from openprovider.exceptions import NoSuchElement
from openprovider.tests import ApiTestCase


class DomainTestCase(ApiTestCase):

    def test_transfer(self):
        try:
            secundary_api = api_factory('test_secundary')
        except KeyError:
            if not hasattr(self, 'skipTest'):  # python 2.6
                return
            self.skipTest("No secundary account configured")

        domain = 'ci-%d.com' % calendar.timegm(dt.now().timetuple())
        primary_handle = 'YN000088-NL'
        secundary_handle = 'YN000101-NL'

        # Register a domain at the primary account
        response = self.api.domain.create_domain_request(
                domain, 1, primary_handle, primary_handle, primary_handle,
                ns_group='dns-openprovider',
        )

        auth_code = str(response.auth_code)

        # Now transfer it to the second account
        response = secundary_api.domain.transfer_domain_request(
                domain, 1, auth_code, secundary_handle, secundary_handle, secundary_handle,
                ns_group='dns-openprovider',
        )
        self.assertEqual(response.status, 'ACT')

        # Should be gone at the first provider
        self.assertRaises(NoSuchElement, self.api.domain.retrieve_domain_request, domain)

        # And be there at the second
        self.assertIsNotNone(secundary_api.domain.retrieve_domain_request(domain))

        # Try to clean up
        try:
            secundary_api.delete_domain_request(domain)
        except:
            pass
