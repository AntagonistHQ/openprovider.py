# coding=utf-8

"""
Wrapper classes for API models. Most of these are thin wrappers over lxml
objectified versions of API responses.
"""

import datetime
import lxml.etree
from openprovider.util import camel_to_snake, snake_to_camel


class Model(object):
    """
    Superclass for all models. Delegates attribute access to a wrapped class.
    """

    def __init__(self, obj=None, **kwargs):
        self._obj = obj
        self._attrs = dict((snake_to_camel(key), value) for (key, value) in kwargs.items())

    def __dir__(self):
        attrs = set(list(self.__dict__.keys()) + [camel_to_snake(key) for key in self._attrs.keys()])
        if self._obj is not None:
            attrs.update(camel_to_snake(t.tag) for t in self._obj.iterchildren())
        return [attr for attr in attrs if not attr.startswith('_')]

    def __getattr__(self, attr):
        """
        Magic for returning an attribute. Will try the attributes of the
        wrapper class first, then attributes in self._attrs, then the attributes
        of the wrapped objectified element.

        Will try a camelCased version of the snake_cased input if the attribute
        contains an underscore. This means foo.company_name will return the same
        as foo.companyName.
        """

        if "_" in attr:
            attr = snake_to_camel(attr)

        if attr in self.__dict__:
            # Check ourselves first to avoid infinite loops
            return getattr(self, attr)

        try:
            return self._attrs[attr]
        except KeyError:
            if self._obj is not None:
                try:
                    return self._obj[attr]
                except (AttributeError, KeyError):
                    pass

        raise AttributeError("Model has no attribute '%s' (tried %r)"
                             % (camel_to_snake(attr), dir(self)))

    def get_elem(self):
        """Returns the wrapped lxml element, if one exists, or else None."""
        return self._obj

    def dump(self, *args, **kwargs):
        """Dumps a representation of the Model on standard output."""
        lxml.etree.dump(self._obj, *args, **kwargs)

    def __repr__(self):
        args = ', '.join('%s=%r' % (attr, getattr(self, attr)) for attr in dir(self))
        return "<%s.%s(%s)>" % (type(self).__module__, type(self).__name__, args)

    def __str__(self):
        return str(lxml.etree.tostring(self._obj)) if self._obj is not None else 'Empty model'


def submodel(klass, key):
    """Shortcut for defining a submodel (has-a relation)."""
    def getter(self):
        return klass(getattr(self._obj, key))
    return property(getter)


def textattribute(attr):
    # TODO: Lots of duplication with __getattr__
    def getter(self):
        try:
            return self._attrs[attr]
        except KeyError:
            if self.get_elem() is not None:
                try:
                    return self.get_elem()[attr].text
                except (AttributeError, KeyError):
                    pass

        raise AttributeError("Model has no attribute '%s' (tried %r)"
                             % (camel_to_snake(attr), dir(self)))

    def setter(self, value):
        self._attrs[attr] = value

    return property(getter, setter)


class Name(Model):
    """
    A person's name.

    initials (required)
        Initials (first letters of first names, first letter of last name)
    firstName (required)
        First name
    prefix (optional)
        Prefix (often occuring in Dutch names; for example van de)
    lastName (required)
        Last name
    """

    def __eq__(self, other):
        attributes = ['initials', 'first_name', 'prefix', 'last_name']
        return all(getattr(self, attr, None) == getattr(other, attr, None) for attr in attributes)

    def __str__(self):
        if getattr(self, "prefix", None):
            return "%s %s %s" % (self.first_name, self.prefix, self.last_name)
        else:
            return "%s %s" % (self.first_name, self.last_name)


class Domain(Model):
    """
    A domain name.

    name (required)
        The domain name without extension
    extension (required)
        The extension part of the domain name
    """

    def __str__(self):
        return "%s.%s" % (self.name, self.extension)


class RegistryDetails(Model):
    """
    A container for a messages from the registry

    messages
        A list of messages
    """

    @property
    def messages(self):
        try:
            return [RegistryMessage(item) for item in self.array[0].item]
        except AttributeError:
            return []


class RegistryMessage(Model):
    """
    A message from the registry

    date
        A datetime object of the message
    message
        The actual message
    """

    message = textattribute("message")

    @property
    def date(self):
        date = None
        try:
            date = self._attrs['date']
        except KeyError:
            if self._obj is not None:
                try:
                    date = self._obj['date']
                except (AttributeError, KeyError):
                    pass

        return datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S') if date else None


class DomainDetails(Model):
    """

    A detailed domain.
    """

    domain = submodel(Domain, "domain")
    registry_details = submodel(RegistryDetails, "registryDetails")

    def __str__(self):
        return str(self.domain)


class Nameserver(Model):
    """
    A nameserver with either an IPv4 or an IPv6 address.

    name (required)
        URI or hostname of the nameserver
    ip (required if no valid ip6)
        IPv4 address of the nameserver
    ip6 (required if no valid ip)
        IPv6 address of the nameserver
    """

    def __str__(self):
        return str(self.name)


class Record(Model):
    """
    A DNS record.

    type (required)
        One of the following data types: A, AAAA, CNAME, MX, SPF, TXT
    name (optional)
        The part of the hostname before the domainname; for example www or ftp
    value (required)
        The value of the record; depending on the type, certain restrictions
        apply; see the FAQ for these restrictions
    prio (optional)
        Priority of the record; required for MX records; ignored for all other
        record types
    ttl (required)
        The Time To Live of the record; this is a value in seconds
    """
    pass


class History(Model):
    """
    Representation of a single modification of a piece of data.

    date (required)
        Date of the modification
    was (required)
        Old contents of the record
    is (required)
        New contents of the record
    """
    pass


class Address(Model):
    """
    A physical street address.

    street (required)
    number (required)
    suffix (optional)
    zipcode (required)
    city (required)
    state (optional)
    country (required)
    """

    def __eq__(self, other):
        attributes = ['street', 'number', 'suffix', 'zipcode', 'city', 'state', 'country']
        return all(getattr(self, attr, None) == getattr(other, attr, None) for attr in attributes)


class Phone(Model):
    """
    An international phone number.

    country_code (required)
    area_code (required)
    subscriber_number (required)
    """

    country_code = textattribute("countryCode")
    area_code = textattribute("areaCode")
    subscriber_number = textattribute("subscriberNumber")

    def __eq__(self, other):
        attributes = ['country_code', 'area_code', 'subscriber_number']
        return all(getattr(self, attr, None) == getattr(other, attr, None) for attr in attributes)

    def __str__(self):
        """Return the string representation of phone number."""
        return "%s %s %s" % (self.country_code, self.area_code, self.subscriber_number)


class Reseller(Model):
    """
    A reseller profile.

    id
    companyName
    address
    phone
    fax
    vatperc
    balance
    reservedBalance
    """

    address = submodel(Address, "address")
    phone = submodel(Phone, "phone")
    fax = submodel(Phone, "fax")


class Customer(Model):
    """
    A customer.

    handle
    companyName
    vat
    name
    gender
    address
    phone
    fax
    email
    """

    name = submodel(Name, "name")
    address = submodel(Address, "address")
    phone = submodel(Phone, "phone")
    fax = submodel(Phone, "fax")
    additional_data = submodel(Model, "additionalData")
    extension_additional_data = submodel(Model, "additionalData")

    def __str__(self):
        return str(self.handle)


class SSLProduct(Model):
    """
    An SSL product.

    id
    name
    brandName
    category
    isMobileSupported
    isIdnSupported
    isSgcSupported
    isWildcardSupported
    isExtendedValidationSupported
    deliveryTime
    freeRefundPeriod
    freeReissuePeriod
    maxPeriod
    numberOfDomains
    encryption
    root
    warranty
    prices
    supportedSoftware
    description
    """
    pass


class SSLOrder(Model):
    """
    An ordered SSL certificate.

    id
    commonName
    productName
    brandName
    status
    orderDate
    activeDate
    expirationDate
    hostNames
    organizationHandle
    administrativeHandle
    technicalHandle
    billingHandle
    emailApprover
    csr
    certificate
    rootCertificate
    """
    pass


class Extension(Model):
    """
    A domain extension (TLD).

    name
    transferAvailable
    isTransferAuthCodeRequired
    domicileAvailable
    usageCount
    description
    prices
    isAuthorizationCodeRequired
    isLockingAllowed
    isTradeAllowed
    restorePrice
    """
    pass
