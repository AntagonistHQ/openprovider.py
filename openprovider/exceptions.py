# coding=utf-8

"""
Openprovider.py-specific exceptions.
"""


class OpenproviderError(Exception):
    """Superclass for all of our exceptions."""

    def __init__(self, message, code=None):
        super(OpenproviderError, self).__init__(message)
        self.code = code


class BadRequest(OpenproviderError):
    """A request didn't pass validation or was denied by Openprovider."""


class ValidationError(BadRequest):
    """A request didn't pass a validation rule."""


class RuleViolation(ValidationError):
    """Executing the request would invalidate a rule."""


class UniqueViolation(RuleViolation):
    """Executing the request would invalidate a uniqueness constraint."""


class BadStateException(RuleViolation):
    """An element is in a state that does not allow your request."""


class InvalidAuthorizationCode(RuleViolation):
    """The authorization code is missing, empty or incorrect."""


class AuthenticationError(BadRequest):
    """Something went wrong while authenticating the request."""


class NoSuchElement(OpenproviderError):
    """The element you tried to retrieve could not be found."""


class InProgress(OpenproviderError):
    """The request is currently being handled but has not finished yet."""


class LimitReached(OpenproviderError):
    """Some limit was reached."""


class InsufficientFunds(LimitReached):
    """Your account does not contain enough funds to execute the request."""


class ServerError(OpenproviderError):
    """Openprovider received your request, but was unable to act on it."""


class ServiceUnavailable(ServerError):
    """The Openprovider API, or part of it, is currently unavailable."""


class Maintenance(ServiceUnavailable):
    """The entire Openprovider API is currently unavailable."""
