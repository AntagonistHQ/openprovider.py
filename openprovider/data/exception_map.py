# coding=utf-8

from openprovider.exceptions import *

MAPPING = {
    307: BadRequest
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
