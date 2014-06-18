# coding=utf-8


class Model(object):
    _obj = None
    attrs = {}

    def __init__(self, obj=None, **kwargs):
        self._obj = obj
        self.attrs.update(kwargs)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        elif attr in self.attrs:
            return self.attrs[attr]
        else:
            return getattr(self._obj, attr)


def submodel(klass, key):
    def getter(self):
        return klass(getattr(self._obj, key))
    return property(getter)


class Name(Model):
    """
    initials (required)
        Initials (first letters of first names, first letter of last name)
    firstName (required)
        First name
    prefix (optional)
        Prefix (often occuring in Dutch names; for example van de)
    lastName (required)
        Last name
    """

    def __str__(self):
        if hasattr(self, "prefix"):
            return " ".join((self.firstName, self.prefix, self.lastName))
        else:
            return " ".join((self.firstName, self.lastName))


class Domain(Model):
    """
    name (required)
        The domain name without extension
    extension (required)
        The extension part of the domain name
    """

    def __str__(self):
        return ".".join((self.name, self.extension))


class Nameserver(Model):
    """
    name (required)
        URI or hostname of the nameserver
    ip (required if no valid ip6)
        IPv4 address of the nameserver
    ip6 (required if no valid ip)
        IPv6 address of the nameserver
    """
    pass


class Record(Model):
    """
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
    street (required)
    number (required)
    suffix (optional)
    zipcode (required)
    city (required)
    state (optional)
    country (required)
    """
    pass


class Phone(Model):
    """
    countryCode (required)
    areaCode (required)
    subscriberNumber (required)
    """
    pass


class Reseller(Model):
    """
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
