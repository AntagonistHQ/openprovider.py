# coding=utf-8

from openprovider.modules import E, common
from openprovider.models import Customer
from openprovider.util import parse_phone_number, snake_to_camel


def _additional_data(data):
    if data is None:
        return None

    element = E.additionalData()
    for key, value in data.items():
        if key == 'birth_date':
            try:
                value = value.strftime('%Y-%m-%d')
            except AttributeError:
                pass
        element.append(E(snake_to_camel(key), value))
    return element


def _extension_additional_data(data):
    if data is None:
        return None

    return E.extensionAdditionalData(E(snake_to_camel(key), value) for key, value in data.items())


def _get_phone_xml(parent, number):
    if not number:
        return ''

    country, area, subscriber = parse_phone_number(number)
    return E(parent,
            E.countryCode(country),
            E.areaCode(area),
            E.subscriberNumber(subscriber),
    )


class CustomerModule(common.Module):
    """Bindings to API methods in the customer module."""

    def create_customer(self, name, gender, address, phone, email, vat=None, fax=None,
                        company_name=None, additional_data=None, extension_additional_data=None):
        """Create a customer"""

        response = self.request(E.createCustomerRequest(
            E.companyName(company_name),
            E.vat(vat),
            E.name(
                E.initials(name.initials),
                E.firstName(name.first_name),
                E.prefix(name.prefix or ''),
                E.lastName(name.last_name),
            ),
            E.gender(gender),
            _get_phone_xml('phone', phone),
            _get_phone_xml('fax', fax),
            E.address(
                E.street(address.street),
                E.number(address.number),
                E.suffix(address.suffix or ''),
                E.zipcode(address.zipcode),
                E.city(address.city),
                E.state(address.state or ''),
                E.country(address.country),
            ),
            E.email(email),
            _additional_data(additional_data),
            _extension_additional_data(extension_additional_data),
        ))

        return str(response.data.handle)

    def delete_customer(self, handle):
        """Delete a customer."""

        self.request(E.deleteCustomerRequest(E.handle(handle)))

        return True

    def modify_customer(self, handle, address, phone, email=None, vat=None, fax=None,
                        company_name=None, additional_data=None, extension_additional_data=None):
        """Modify a customer."""

        self.request(E.modifyCustomerRequest(
            E.handle(handle),
            E.vat(vat or ''),
            _get_phone_xml('phone', phone),
            _get_phone_xml('fax', fax),
            E.address(
                E.street(address.street),
                E.number(address.number),
                E.suffix(address.suffix or ''),
                E.zipcode(address.zipcode),
                E.city(address.city),
                E.state(address.state or ''),
                E.country(address.country),
            ),
            E.email(email or ''),
            _additional_data(additional_data),
            _extension_additional_data(extension_additional_data),
        ))

        return True

    def search_customer(self, limit=100, offset=0, email_pattern=None, last_name_pattern=None,
            company_name_pattern=None, with_additional_data=False):
        """Search the list of customers."""

        response = self.request(E.searchCustomerRequest(
            E.limit(limit),
            E.offset(offset),
            E.emailPattern(email_pattern or ''),
            E.lastNamePattern(last_name_pattern or ''),
            E.companyNamePattern(company_name_pattern or ''),
            E.withAdditionalData(int(with_additional_data)),
        ))

        return response.as_models(Customer)

    def retrieve_customer(self, handle, with_additional_data=False):
        """Retrieve information of an existing customer."""

        response = self.request(E.retrieveCustomerRequest(
            E.handle(handle),
            E.withAdditionalData(int(with_additional_data)),
        ))

        return response.as_model(Customer)
