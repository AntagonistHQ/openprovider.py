# coding=utf-8

"""Contains tests both for the models system and for the models themselves."""

from openprovider.models import Model, Name, Domain, Phone


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
