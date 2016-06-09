from __future__ import absolute_import

import pytest
import random

from . import betamaxed
from betamax import Betamax
from datetime import date
from faker import Factory
from openprovider.exceptions import NoSuchElement
from openprovider.models import Address, Name, Phone
from openprovider.util import parse_phone_number


fake = Factory.create('nl_NL')


@pytest.fixture
def name():
    first_name = fake.first_name()
    initials = '.'.join(n[0] for n in first_name.split()) + '.'
    prefix = ''  # TODO: faker doesn't have prefixes like we use them
    last_name = fake.last_name()
    return Name(initials=initials, first_name=first_name, prefix=prefix, last_name=last_name)


@pytest.fixture
def gender():
    return 'M' if random.random() < 0.5 else 'F'


@pytest.fixture
def address():
    street = fake.street_name()
    number = random.randint(1, 100)
    suffix = None  # TODO: handle sometimes empty values with placeholders
    zipcode = fake.postcode()
    state = fake.province()
    city = fake.city()
    country = 'NL'
    return Address(street=street, number=number, suffix=suffix, zipcode=zipcode, state=state,
                   city=city, country=country)


@pytest.fixture
def phone():
    return '+31.%08d' % random.randint(1, 99999999999)


@pytest.fixture
def email():
    return fake.email()


def _get_phone_object(number):
    country, area, subscriber = parse_phone_number(number)
    return Phone(country_code=country, area_code=area, subscriber_number=subscriber)


def _to_placeholder(key, value):
    return {'placeholder': '>|%s|<' % key.upper(), 'replace': u'>%s<' % value}


def _to_placeholders(**kwargs):
    for prefix, obj in kwargs.items():
        if isinstance(obj, basestring):
            yield _to_placeholder(prefix, obj)
        else:
            for attr in dir(obj):
                value = getattr(obj, attr)
                if value:
                    yield _to_placeholder('%s_%s' % (prefix, attr), value)


@betamaxed
def test_customer_search(api):
    r = api.customers.search_customer()
    assert len(r) >= 1


@betamaxed
def test_customer_search_non_existing(api):
    r = api.customers.search_customer(email_pattern="doesntexist.com")
    assert len(r) == 0


def test_crud_with_minimal_data(api, name, gender):
    old_address = address()
    new_address = address()
    assert old_address != new_address
    old_phone = phone()
    new_phone = phone()
    assert old_phone != new_phone
    old_email = email()
    new_email = email()
    assert old_email != new_email

    placeholders = list(_to_placeholders(name=name, gender=gender,
            old_phone=_get_phone_object(old_phone), new_phone=_get_phone_object(new_phone),
            old_email=old_email, new_email=new_email, old_address=old_address, new_address=new_address))

    with Betamax(api.session) as recorder:
        with recorder.use_cassette('test_customer_crud_1', placeholders=placeholders):
            handle = api.customer.create_customer(name, gender, old_address, old_phone, old_email)
            assert isinstance(handle, str)

        placeholders.append(_to_placeholder('handle', handle))
        with recorder.use_cassette('test_customer_crud_2', placeholders=placeholders):
            customer = api.customer.retrieve_customer(handle)
            assert customer.name == name
            assert customer.address == old_address
            assert customer.phone == _get_phone_object(old_phone)
            assert customer.email == old_email

            result = api.customer.modify_customer(handle, new_address, new_phone, new_email)
            assert result is True

        with recorder.use_cassette('test_customer_crud_3', placeholders=placeholders):
            customer = api.customer.retrieve_customer(handle)
            assert customer.name == name
            assert customer.address == new_address
            assert customer.phone == _get_phone_object(new_phone)
            assert customer.email == new_email

            result = api.customer.delete_customer(handle)
            assert result is True

        with recorder.use_cassette('test_customer_crud_4'):
            with pytest.raises(NoSuchElement):
                api.customer.retrieve_customer(handle)


def test_customer_modify_doesnt_wipe_additional_data(api, name, gender, address, phone, email):
    additional_data = {
            'birth_date': date(1980, 5, 10),
    }

    placeholders = list(_to_placeholders(name=name, gender=gender, address=address, phone=phone, email=email))

    with Betamax(api.session) as recorder:
        with recorder.use_cassette('test_customer_modify_doesnt_wipe_1', placeholders=placeholders):
            handle = api.customer.create_customer(name, gender, address, phone, email,
                                                  additional_data=additional_data)
            assert isinstance(handle, str)

        placeholders.append(_to_placeholder('handle', handle))
        with recorder.use_cassette('test_customer_modify_doesnt_wipe_2', placeholders=placeholders):
            customer = api.customer.retrieve_customer(handle, with_additional_data=True)
            assert customer.additional_data.birth_date == '1980-05-10'

            result = api.customer.modify_customer(handle, address, phone, email)
            assert result is True

        with recorder.use_cassette('test_customer_modify_doesnt_wipe_3', placeholders=placeholders):
            customer = api.customer.retrieve_customer(handle, with_additional_data=True)
            assert customer.additional_data.birth_date == '1980-05-10'

            result = api.customer.delete_customer(handle)
            assert result is True

        with recorder.use_cassette('test_customer_modify_doesnt_wipe_4', placeholders=placeholders):
            with pytest.raises(NoSuchElement):
                api.customer.retrieve_customer(handle)
