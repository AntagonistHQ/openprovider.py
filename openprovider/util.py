# coding=utf-8

import re

def camel_to_snake(string):
    """Converts camelCaseString to snake_case_string."""
    return re.sub('([A-Z]+)', r'_\1', string).lower()

def snake_to_camel(value):
    """Converts snake_case_string to camelCaseString."""
    camel = "".join(word.title() for word in value.split("_"))
    return value[:1].lower() + camel[1:]