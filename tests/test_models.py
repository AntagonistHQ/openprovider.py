# coding=utf-8

"""Contains tests both for the models system and for the models themselves."""

import pytest

from openprovider.models import Model, Name, Domain, Phone, Address


def test_model_construct_kwargs():
    """Tests construction of a Model by keyword arguments."""
    mod = Model(foo="foo", bar=Model(baz="baz"))
    assert mod.foo == "foo"
    assert mod.bar.baz == "baz"


def test_model_snake_case():
    """Tests Model's case-aliasing magic."""
    mod = Model(spam_and_eggs="Spam, spam, glorious spam")
    assert mod.spam_and_eggs == "Spam, spam, glorious spam"


def test_model_camel_case():
    mod = Model(spamAndEggs="Spam, spam, glorious spam")
    assert mod.spamandeggs == "Spam, spam, glorious spam"


def test_name_str():
    """Tests the Name model and its string conversion."""
    leo = Name(first_name="Leonardo", prefix="da", last_name="Vinci")
    assert str(leo) == "Leonardo da Vinci"


@pytest.mark.parametrize("first,second", [
    (Name(), Name()),
    (
        Name(first_name="Leonardo", prefix="da", last_name="Vinci"),
        Name(first_name="Leonardo", prefix="da", last_name="Vinci")
    ),
    (
        Name(first_name="Leonardo", prefix="da", last_name="Vinci", initials=None),
        Name(first_name="Leonardo", prefix="da", last_name="Vinci")
    ),
    (
        Name(first_name="Leonardo", prefix="da", last_name="Vinci", initials=''),
        Name(first_name="Leonardo", prefix="da", last_name="Vinci", initials='')
    ),
    (Phone(), Phone()),
    (
        Phone(country_code='31', area_code='53', subscriber_number='1234567'),
        Phone(country_code='31', area_code='53', subscriber_number='1234567')
    ),
    (Address(), Address()),
    (
        Address(street='street', number=123, suffix='', zipcode='1234AB', city='Amsterdam', state='Noord Holland', country='NL'),
        Address(street='street', number=123, suffix='', zipcode='1234AB', city='Amsterdam', state='Noord Holland', country='NL'),
    ),
])
def test_equal_with_equal(first, second):
    assert first == second


@pytest.mark.parametrize("first,second", [
    (Name(first_name='Leo'), Name()),
    (
        Name(first_name="Leonardo", prefix="da", last_name="Vinci"),
        Name(first_name="Leonardo", prefix="da", last_name="Vinci", initials='')
    ),
    (
        Name(first_name="Leonardo", prefix="da", last_name="Vinci", initials=None),
        Name(first_name="Leonardo", prefix="da", last_name="Vinci", initials='')
    ),
    (Phone(country_code=31), Phone()),
    (Address(country='NL'), Address()),
])
def test_equal_with_unequal(first, second):
    assert first != second


def test_domain_str():
    """Tests the Domain model and its string conversion."""
    dom = Domain(name="example", extension="com")
    assert str(dom) == "example.com"


def test_phone_str():
    """Tests the Phone model and its string conversion."""
    country = "31"
    area = "026"
    subscr = "3557772"

    p = Phone(country_code=country, area_code=area, subscriber_number=subscr)
    assert str(p), "31 026 3557772"
