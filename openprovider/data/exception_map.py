# coding=utf-8

from openprovider.exceptions import *

MAPPING = {
    307: BadRequest,   # Invalid domain extension
    501: BadRequest,   # Domain name too short
}


def from_code(code):
    """
    Return the specific exception class for the given code, or OpenproviderError
    if no specific exception class is available.
    """
    if code in MAPPING:
        return MAPPING[code]
    else:
        return OpenproviderError
