# coding=utf-8

"""
Openprovider.py-specific exceptions.
"""

class OpenproviderError(Exception):
    """Superclass for all of our exceptions."""
    pass


class BadRequest(OpenproviderError):
    """A request didn't pass validation or was denied by Openprovider."""
    pass


class ServiceUnavailable(OpenproviderError):
    """The Openprovider API is currently undergoing maintenance."""
    pass

