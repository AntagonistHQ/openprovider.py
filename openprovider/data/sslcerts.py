# coding=utf-8

"""SSL-related constants and enums."""


class CertType(object):
    """Constants that can be used as SSL certificate product ID's."""

    VERISIGN_SS = 1
    VERISIGN_SS_PRO = 2
    VERISIGN_SS_EV = 3
    VERISIGN_SS_PRO_EV = 4
    GEOTRUST_QUICKSSL_PREMIUM_DV = 8
    GEOTRUST_TBID = 9
    GEOTRUST_TBID_EV = 10
    GEOTRUST_TBID_MULTI_DOMAIN = 34
    GEOTRUST_TBID_EV_MULTI_DOMAIN = 30
    GEOTRUST_TBID_WILDCARD = 11
    THAWTE_SSL_123 = 14
    THAWTE_WEB_SERVER = 15
    THAWTE_WEB_SERVER_EV = 16
    THAWTE_WEB_SERVER_WILDCARD = 17
    THAWTE_SGC_SUPERCERT = 18
    COMODO_ESSENTIALSSL = 31
    COMODO_INSTANTSSL = 20
    COMODO_INSTANTSSL_PRO = 21
    COMODO_PREMIUMSSL = 22
    COMODO_EV_SSL = 24
    COMODO_EV_SGC_SSL_EV = 27
    COMODO_INSTANT_SGC_SSL = 25
    COMODO_UCC = 28
    COMODO_EVSSL_MULTI_DOMAIN = 33
    COMODO_ESSENTIALSSL_WILDCARD = 32
    COMODO_PREMIUMSSL_WILDCARD = 23
    COMODO_INSTANT_SGC_WILDCARD_SSL = 26
    RAPIDSSL = 5
    RAPIDSSL_WILDCARD = 6

    WILDCARD_CERTIFICATES = (
        GEOTRUST_TBID_WILDCARD,
        THAWTE_WEB_SERVER_WILDCARD,
        COMODO_ESSENTIALSSL_WILDCARD,
        COMODO_PREMIUMSSL_WILDCARD,
        COMODO_INSTANT_SGC_WILDCARD_SSL,
        RAPIDSSL_WILDCARD)

    DV_CERTIFICATES = (
        GEOTRUST_QUICKSSL_PREMIUM_DV,
        THAWTE_SSL_123,
        COMODO_ESSENTIALSSL,
        RAPIDSSL)

    OV_CERTIFICATES = (
        VERISIGN_SS,
        GEOTRUST_TBID,
        THAWTE_WEB_SERVER,
        COMODO_PREMIUMSSL,
        COMODO_INSTANTSSL_PRO,
        COMODO_INSTANTSSL)

    EV_CERTIFICATES = (
        VERISIGN_SS_EV,
        GEOTRUST_TBID_EV,
        THAWTE_WEB_SERVER_EV,
        COMODO_EV_SSL)

    SGC_CERTIFICATES = (
        VERISIGN_SS_PRO_EV,
        VERISIGN_SS_PRO,
        THAWTE_SGC_SUPERCERT,
        COMODO_INSTANT_SGC_WILDCARD_SSL,
        COMODO_EV_SGC_SSL_EV,
        COMODO_INSTANT_SGC_SSL)

    MULTI_CERTIFICATES = (
        GEOTRUST_TBID_EV_MULTI_DOMAIN,
        GEOTRUST_TBID_MULTI_DOMAIN,
        COMODO_EVSSL_MULTI_DOMAIN,
        COMODO_UCC)

    @staticmethod
    def is_wildcard(cert):
        """Returns True if this is a wildcard certificate."""
        return cert in CertType.WILDCARD_CERTIFICATES

    @staticmethod
    def is_dv(cert):
        """Returns True if this is a domain-validated certificate."""
        return cert in CertType.DV_CERTIFICATES

    @staticmethod
    def is_ov(cert):
        """Returns True if this is an organization-validated certificate."""
        return cert in CertType.OV_CERTIFICATES

    @staticmethod
    def is_ev(cert):
        """Returns True if this is an Extended validation cert."""
        return cert in CertType.EV_CERTIFICATES

    @staticmethod
    def is_sgc(cert):
        """Returns True if this is a server-gated cryptography certificate."""
        return cert in CertType.SGC_CERTIFICATES

    @staticmethod
    def is_multidomain(cert):
        """Returns True if this is a multi-domain certificate."""
        return cert in CertType.MULTI_CERTIFICATES
