from betamax import Betamax
from textwrap import dedent
from openprovider.data.sslcerts import CertTypes
from . import betamaxed


@betamaxed
def test_create_with_minimal_parameters(api):
    csr = dedent("""
    -----BEGIN CERTIFICATE REQUEST-----
    MIICnTCCAYUCAQAwWDELMAkGA1UEBhMCTkwxFTATBgNVBAcMDERlZmF1bHQgQ2l0
    eTEcMBoGA1UECgwTRGVmYXVsdCBDb21wYW55IEx0ZDEUMBIGA1UEAwwLZXhhbXBs
    ZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCySUcRJiuMSnwV
    OcShDz3PhfXI5vCoQ6ve2xsu1fO7V9du2DtSqpdmxZaKs/2MEV6gRVKsPJFx33J8
    GOBS6af2rILvKZ2Lr+IKiAdh5mX8tmZfuQLEXYlpluJphqMXQ68cTu8Pg0M85TXv
    ECXa8cIKAp6+5bfoz84vzb+I69jUaMkgZllS9P3xSaWM7uNTRyPJEBu6jOg09vHR
    aPqXE8HFCRv3P+Y+hnt1Kph79Ex7wf1/dtDV8H5/gWxWhk6MxpEtIdo/taADFFvK
    FZRip0uypak1F48Vwjaql7hchZ37tCeSDMTkxoS98Pe4oU+FMnQOEXc3zebvLT7W
    1mWwcXtnAgMBAAGgADANBgkqhkiG9w0BAQsFAAOCAQEAPIlaXOnug1Oi9EhLPb+a
    DwZJVp+jaPE43i9yJcxQK7okUznVwEhVrrGnwWnvbN+HyAtK7or08osXnfho40gA
    vzWz9gEMnO4xjIdSow28tFnEwfDihhQdFgxCrQI72VZM/kPxpjVLMEWNXwjM5gAy
    SdO1lquLgTm/POounk8tJwsHUfGqpUU3Vo3iXz5RALJo2UGTdJO0n81aPVDK7ni1
    mukvRBCIYt8LLe7DYcBceT7qxkHOdFOTmpgEKVYcr26dQ1vmkWwe5Zoj0eXGxkfx
    AgjC+fsMiuD0XrWSMi82pjhLqlqxY7FxL0N57sypJv5btH3F6mgKYu9Qr1+My/k0
    hg==
    -----END CERTIFICATE REQUEST-----""").lstrip()
    order_id = api.ssl.create(product_id=CertTypes.COMODO_ESSENTIALSSL.product_id, period=1,
                              csr=csr, software_id='linux', organization_handle='YN000088-NL',
                              approver_email='hostmaster@example.com')
    assert isinstance(order_id, int)
    assert order_id > 0


@betamaxed
def test_create_with_all_parameters(api):
    csr = dedent("""
    -----BEGIN CERTIFICATE REQUEST-----
    MIICnTCCAYUCAQAwWDELMAkGA1UEBhMCTkwxFTATBgNVBAcMDERlZmF1bHQgQ2l0
    eTEcMBoGA1UECgwTRGVmYXVsdCBDb21wYW55IEx0ZDEUMBIGA1UEAwwLZXhhbXBs
    ZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCySUcRJiuMSnwV
    OcShDz3PhfXI5vCoQ6ve2xsu1fO7V9du2DtSqpdmxZaKs/2MEV6gRVKsPJFx33J8
    GOBS6af2rILvKZ2Lr+IKiAdh5mX8tmZfuQLEXYlpluJphqMXQ68cTu8Pg0M85TXv
    ECXa8cIKAp6+5bfoz84vzb+I69jUaMkgZllS9P3xSaWM7uNTRyPJEBu6jOg09vHR
    aPqXE8HFCRv3P+Y+hnt1Kph79Ex7wf1/dtDV8H5/gWxWhk6MxpEtIdo/taADFFvK
    FZRip0uypak1F48Vwjaql7hchZ37tCeSDMTkxoS98Pe4oU+FMnQOEXc3zebvLT7W
    1mWwcXtnAgMBAAGgADANBgkqhkiG9w0BAQsFAAOCAQEAPIlaXOnug1Oi9EhLPb+a
    DwZJVp+jaPE43i9yJcxQK7okUznVwEhVrrGnwWnvbN+HyAtK7or08osXnfho40gA
    vzWz9gEMnO4xjIdSow28tFnEwfDihhQdFgxCrQI72VZM/kPxpjVLMEWNXwjM5gAy
    SdO1lquLgTm/POounk8tJwsHUfGqpUU3Vo3iXz5RALJo2UGTdJO0n81aPVDK7ni1
    mukvRBCIYt8LLe7DYcBceT7qxkHOdFOTmpgEKVYcr26dQ1vmkWwe5Zoj0eXGxkfx
    AgjC+fsMiuD0XrWSMi82pjhLqlqxY7FxL0N57sypJv5btH3F6mgKYu9Qr1+My/k0
    hg==
    -----END CERTIFICATE REQUEST-----""").lstrip()
    order_id = api.ssl.create(product_id=CertTypes.COMODO_ESSENTIALSSL.product_id, period=1,
                              csr=csr, software_id='linux', organization_handle='YN000088-NL',
                              approver_email='hostmaster@example.com',
                              signature_hash_algorithm='sha2',
                              domain_validation_methods={'example.com': 'dns'},
                              technical_handle='YN000088-NL')
    assert isinstance(order_id, int)
    assert order_id > 0


@betamaxed
def test_decode_valid_csr(api):
    csr = dedent("""
    -----BEGIN CERTIFICATE REQUEST-----
    MIICnTCCAYUCAQAwWDELMAkGA1UEBhMCTkwxFTATBgNVBAcMDERlZmF1bHQgQ2l0
    eTEcMBoGA1UECgwTRGVmYXVsdCBDb21wYW55IEx0ZDEUMBIGA1UEAwwLZXhhbXBs
    ZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCySUcRJiuMSnwV
    OcShDz3PhfXI5vCoQ6ve2xsu1fO7V9du2DtSqpdmxZaKs/2MEV6gRVKsPJFx33J8
    GOBS6af2rILvKZ2Lr+IKiAdh5mX8tmZfuQLEXYlpluJphqMXQ68cTu8Pg0M85TXv
    ECXa8cIKAp6+5bfoz84vzb+I69jUaMkgZllS9P3xSaWM7uNTRyPJEBu6jOg09vHR
    aPqXE8HFCRv3P+Y+hnt1Kph79Ex7wf1/dtDV8H5/gWxWhk6MxpEtIdo/taADFFvK
    FZRip0uypak1F48Vwjaql7hchZ37tCeSDMTkxoS98Pe4oU+FMnQOEXc3zebvLT7W
    1mWwcXtnAgMBAAGgADANBgkqhkiG9w0BAQsFAAOCAQEAPIlaXOnug1Oi9EhLPb+a
    DwZJVp+jaPE43i9yJcxQK7okUznVwEhVrrGnwWnvbN+HyAtK7or08osXnfho40gA
    vzWz9gEMnO4xjIdSow28tFnEwfDihhQdFgxCrQI72VZM/kPxpjVLMEWNXwjM5gAy
    SdO1lquLgTm/POounk8tJwsHUfGqpUU3Vo3iXz5RALJo2UGTdJO0n81aPVDK7ni1
    mukvRBCIYt8LLe7DYcBceT7qxkHOdFOTmpgEKVYcr26dQ1vmkWwe5Zoj0eXGxkfx
    AgjC+fsMiuD0XrWSMi82pjhLqlqxY7FxL0N57sypJv5btH3F6mgKYu9Qr1+My/k0
    hg==
    -----END CERTIFICATE REQUEST-----""").lstrip()

    key = dedent("""
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsklHESYrjEp8FTnEoQ89
    z4X1yObwqEOr3tsbLtXzu1fXbtg7UqqXZsWWirP9jBFeoEVSrDyRcd9yfBjgUumn
    9qyC7ymdi6/iCogHYeZl/LZmX7kCxF2JaZbiaYajF0OvHE7vD4NDPOU17xAl2vHC
    CgKevuW36M/OL82/iOvY1GjJIGZZUvT98UmljO7jU0cjyRAbuozoNPbx0Wj6lxPB
    xQkb9z/mPoZ7dSqYe/RMe8H9f3bQ1fB+f4FsVoZOjMaRLSHaP7WgAxRbyhWUYqdL
    sqWpNRePFcI2qpe4XIWd+7QnkgzE5MaEvfD3uKFPhTJ0DhF3N83m7y0+1tZlsHF7
    ZwIDAQAB
    -----END PUBLIC KEY-----
    """).lstrip()

    result = api.ssl.decode_csr(csr)
    assert result['publicKey']['bits'] == 2048
    assert result['publicKey']['key'] == key
    assert result['subject']['commonName'] == 'example.com'
    assert result['subject']['organization'] == 'Default Company Ltd'
    assert result['subject']['unit'] == ''
    assert result['subject']['locality'] == 'Default City'
    assert result['subject']['state'] == ''
    assert result['subject']['country'] == 'NL'
    assert result['subject']['email'] == ''
    assert result['signatureHashAlgorithm'] == 'sha256WithRSAEncryption'
    assert result['subjectAlternativeName'] == ''
    assert result['domainNamesCount'] == 1


@betamaxed
def test_search_product(api):
    """Test for the SSL product search method."""
    result = api.ssl.search_product()
    assert isinstance(result, list)
    assert len(result) > 0
    assert result[0].id is not None


@betamaxed
def test_ssl_retrieve_product(api):
    """Test for retrieving details on a single product."""
    res = api.ssl.retrieve_product(CertTypes.COMODO_EV_SSL.product_id)
    assert res.id == CertTypes.COMODO_EV_SSL.product_id


def test_ssl_order(api):
    """Test that orders a SSL certificate, then cancels it."""

    csr = dedent("""
    -----BEGIN CERTIFICATE REQUEST-----
    MIICzjCCAbYCAQAwgYgxCzAJBgNVBAYTAk5MMRMwEQYDVQQIDApPdmVyaWpzc2Vs
    MREwDwYDVQQHDAhFbnNjaGVkZTEYMBYGA1UECgwPQW50YWdvbmlzdCBCLlYuMSEw
    HwYDVQQLDBhPUEVOUFJPVklERVIgUFkgVEVTVCBDU1IxFDASBgNVBAMMC2V4YW1w
    bGUuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7WvbK/VDTxc/
    9DFkYreQNZo6j+0TrFFX1kqopS/COkkTaNY4xl7B/bq/CBS34nfjRT8x05RhyP2F
    mrNf6fZzl+8boQwJ4eVIDMjTNNecAsKrDTlZqwtvauPPEZ0pV7v6fxO+QOMn1uJq
    ZV7F+vdZ0IUihFUNwQoh9RaIoGtkaAiv1fgH/nrUuci/A9PqH2IBPRf9cCiIt1eK
    WCMXvWFzxkTATPVO35GByjN1GyMgRwTVrP53MKGAUOvbI4awS5x/ByKgigFhfLwr
    M86SSz1ZejlwZ7WqXFgPardMXOYt63ybKASanUTEUAgaEeK/9eL/sKQvEB0tBHbK
    e4uEksNsxwIDAQABoAAwDQYJKoZIhvcNAQELBQADggEBANlOjT4ddIgf9Zg1kR6p
    zbSfwuKLjS/w5RrnT5HliSTRUT/N8tNd2hRiukPqayJGhxtUIvyPdJTYUumIOnhu
    9ZZJcQJQDr5mvhP9hWn4/4yxOuZRd9q7DeoPSDRTkz7MuygoXQGt0ehOMcZBsfUC
    Uqx6ReCDz9PqgCa75XPL041SVot0RVswiiV54JRN0/cKzaItvtvinf0bPpPA1IWX
    qYm2QyYYJ8ayAsIw64YukRSOXp+escQ4rLfR1Un+QvgJM05x47jX8JivO3utexca
    cDJkVtg8DtoP1O1iF+xhNcHeWXUNO+PWHS9jIjL2Ofb78LjMpBjnB7C1L8rYxxg8
    cXU=
    -----END CERTIFICATE REQUEST-----
    """).strip()

    cert = CertTypes.COMODO_ESSENTIALSSL.product_id
    cust = "YN000088-NL"

    cname = "example.com"
    mail1 = "admin@example.com"
    mail2 = "administrator@example.com"

    with Betamax(api.session).use_cassette('test_ssl_order_decode_csr'):
        decoded_csr = api.ssl.decode_csr(csr)
        assert cname == decoded_csr.subject.commonName

    with Betamax(api.session).use_cassette('test_ssl_order_create'):
        oid = api.ssl.create(cert, 1, csr, "linux", cust, mail1)
        assert isinstance(oid, int)
        assert oid > 0

    with Betamax(api.session).use_cassette('test_ssl_order_retrieve'):
        assert cust == api.ssl.retrieve_order(oid).organizationHandle

    with Betamax(api.session).use_cassette('test_ssl_order_change_approver'):
        assert oid == api.ssl.change_approver_email_address(oid, mail2)

    with Betamax(api.session).use_cassette('test_ssl_order_change_resend'):
        assert oid == api.ssl.resend_approver_email(oid)

    with Betamax(api.session).use_cassette('test_ssl_order_change_cancel'):
        assert oid == api.ssl.cancel(oid)


@betamaxed
def test_ssl_approver_email(api):
    """Test for retrieving a list of allowed approver email addresses."""
    cert = CertTypes.COMODO_ESSENTIALSSL.product_id
    emails = api.ssl.retrieve_approver_email_list("example.com", cert)
    assert "admin@example.com" in emails
