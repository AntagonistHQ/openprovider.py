# coding=utf-8


class Model(object):
    _obj = None

    def __init__(self, obj=None):
        self._obj = obj

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        else:
            return getattr(self._obj, attr)


def submodel(klass, key):
    def getter(self):
        return klass(getattr(self._obj, key))
    return property(getter)


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
