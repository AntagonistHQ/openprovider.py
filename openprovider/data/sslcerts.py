# coding=utf-8

"""SSL-related constants and enums."""


class CertType(object):
    """A certificate type that can be purchased from OpenProvider."""

    product_id = 0
    vendor = ""
    name = ""
    validation = None
    is_multi = False
    is_sgc = False
    is_wildcard = False

    def __init__(self, product_id, vendor, name, validation, **kwargs):
        self.product_id = product_id
        self.vendor = vendor
        self.name = name
        self.validation = validation
        self.__dict__.update(kwargs)


class CertTypes(object):
    """
    A class that contains constants that can be used as SSL certificate product
    ID's.
    """

    VERISIGN_SS = CertType(1, "Verisign", "Secure Site", "OV")
    VERISIGN_SS = CertType(1, "", "", "")
    VERISIGN_SS_PRO = CertType(2, "", "", "")
    VERISIGN_SS_EV = CertType(3, "", "", "")
    VERISIGN_SS_PRO_EV = CertType(4, "", "", "")
    GEOTRUST_QUICKSSL_PREMIUM_DV = CertType(8, "", "", "")
    GEOTRUST_TBID = CertType(9, "", "", "")
    GEOTRUST_TBID_EV = CertType(10, "", "", "")
    GEOTRUST_TBID_MULTI_DOMAIN = CertType(34, "", "", "")
    GEOTRUST_TBID_EV_MULTI_DOMAIN = CertType(30, "", "", "")
    GEOTRUST_TBID_WILDCARD = CertType(11, "", "", "")
    THAWTE_SSL_123 = CertType(14, "", "", "")
    THAWTE_WEB_SERVER = CertType(15, "", "", "")
    THAWTE_WEB_SERVER_EV = CertType(16, "", "", "")
    THAWTE_WEB_SERVER_WILDCARD = CertType(17, "", "", "")
    THAWTE_SGC_SUPERCERT = CertType(18, "", "", "")
    COMODO_ESSENTIALSSL = CertType(31, "", "", "")
    COMODO_INSTANTSSL = CertType(20, "", "", "")
    COMODO_INSTANTSSL_PRO = CertType(21, "", "", "")
    COMODO_PREMIUMSSL = CertType(22, "", "", "")
    COMODO_EV_SSL = CertType(24, "", "", "")
    COMODO_EV_SGC_SSL_EV = CertType(27, "", "", "")
    COMODO_INSTANT_SGC_SSL = CertType(25, "", "", "")
    COMODO_UCC = CertType(28, "", "", "")
    COMODO_EVSSL_MULTI_DOMAIN = CertType(33, "", "", "")
    COMODO_ESSENTIALSSL_WILDCARD = CertType(32, "", "", "")
    COMODO_PREMIUMSSL_WILDCARD = CertType(23, "", "", "")
    COMODO_INSTANT_SGC_WILDCARD_SSL = CertType(26, "", "", "")
    RAPIDSSL = CertType(5, "", "", "")
    RAPIDSSL_WILDCARD = CertType(6, "", "", "")

    @classmethod
    def all(cls):
        return filter(lambda x: isinstance(x, CertType), cls.__dict__.values())

    @classmethod
    def dv_certs(cls):
        return filter(lambda x: x.is_dv, cls.all())
