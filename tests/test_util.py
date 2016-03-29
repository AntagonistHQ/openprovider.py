# coding=utf-8

"""Contains tests for the utilities module."""

import pytest
from openprovider.util import camel_to_snake, snake_to_camel, parse_phone_number


@pytest.mark.parametrize("value,expected", [
    ("", ""),
    ("name", "name"),
    ("companyName", "company_name"),
    ("spamAndEggs", "spam_and_eggs"),
])
def test_camel_to_snake(value, expected):
    assert camel_to_snake(value) == expected


def test_snake_camel_snake():
    assert camel_to_snake(snake_to_camel("country_code")) == "country_code"


@pytest.mark.parametrize("value,expected", [
    ("", ""),
    ("name", "name"),
    ("company_name", "companyName"),
    ("spam_and_eggs", "spamAndEggs"),
    ("countryCode", "countrycode"),  # This may not be what the user wants, but it is what it is
])
def test_snake_to_camel(value, expected):
    assert snake_to_camel(value) == expected


def test_camel_snake_camel():
    assert snake_to_camel(camel_to_snake("countryCode")), "countryCode"


@pytest.mark.parametrize("number,expected", [
    ("+1.5552368", ("+1", "5", "552368")),
    (("+1", "867", "5309"), ("+1", "867", "5309")),
])
def test_parse_phone_number_valid_numbers(number, expected):
    assert parse_phone_number(number) == expected


@pytest.mark.parametrize("number", ["123", "+31.", [1, 2, 3, 4], object()])
def test_parse_phone_number_invalid_numbers(number):
    with pytest.raises(ValueError):
        parse_phone_number(number)
