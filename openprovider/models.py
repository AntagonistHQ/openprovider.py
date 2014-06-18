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
