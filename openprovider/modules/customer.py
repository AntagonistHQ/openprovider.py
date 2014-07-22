# coding=utf-8

from openprovider.modules import common
from openprovider.models import Customer
from openprovider.util import parse_phone_number


def _get_phone_xml(e, parent, number):
    if not number:
        return ''

    country, area, subscriber = parse_phone_number(number)
    return parent(
            e.countryCode(country),
            e.areaCode(area),
            e.subscriberNumber(subscriber),
    )


class CustomerModule(common.Module):
    """Bindings to API methods in the customer module."""

    def create_customer(self, name, gender, address, phone, email, vat=None, fax=None,
                        company_name=None, additional_data={}):
        """Create a customer"""

        e = self.e

        response = self.request(e.createCustomerRequest(
            e.companyName(company_name),
            e.vat(vat),
            e.name(
                e.initials(name.initials),
                e.firstName(name.first_name),
                e.prefix(name.prefix or ''),
                e.lastName(name.last_name),
            ),
            e.gender(gender),
            _get_phone_xml(e, e.phone, phone),
            _get_phone_xml(e, e.fax, fax),
            e.address(
                e.street(address.street),
                e.number(address.number),
                e.suffix(address.suffix or ''),
                e.zipcode(address.zipcode),
                e.city(address.city),
                e.state(address.state or ''),
                e.country(address.country),
            ),
            e.email(email),
            e.additionalData(*[e(key, value) for key, value in additional_data.items()]),
        ))

        return str(response.data.handle)

    def delete_customer(self, handle):
        """Delete a customer."""

        e = self.e

        self.request(e.deleteCustomerRequest(e.handle(handle)))

        return True

    def modify_customer(self, handle, address, phone, email=None, vat=None, fax=None,
                        company_name=None, additional_data={}):
        """Modify a customer."""

        e = self.e

        self.request(e.modifyCustomerRequest(
            e.handle(handle),
            e.vat(vat or ''),
            _get_phone_xml(e, e.phone, phone),
            _get_phone_xml(e, e.fax, fax),
            e.address(
                e.street(address.street),
                e.number(address.number),
                e.suffix(address.suffix or ''),
                e.zipcode(address.zipcode),
                e.city(address.city),
                e.state(address.state or ''),
                e.country(address.country),
            ),
            e.email(email or ''),
            e.additionalData(*[e(key, value) for key, value in additional_data.items()]),
        ))

        return True

    def search_customer(self, limit=100, offset=0, email_pattern=None, last_name_pattern=None,
            company_name_pattern=None, with_additional_data=False):
        """Search the list of customers."""

        e = self.e

        response = self.request(e.searchCustomerRequest(
            e.limit(limit),
            e.offset(offset),
            e.emailPattern(email_pattern or ''),
            e.lastNamePattern(last_name_pattern or ''),
            e.companyNamePattern(company_name_pattern or ''),
            e.withAdditionalData(int(with_additional_data)),
        ))

        return response.as_models(Customer)

    def retrieve_customer(self, handle, with_additional_data=False):
        """Retrieve information of an existing customer."""

        e = self.e

        response = self.request(e.retrieveCustomerRequest(
            e.handle(handle),
            e.withAdditionalData(int(with_additional_data)),
        ))

        return response.as_model(Customer)
