from textwrap import dedent
from openprovider.data.sslcerts import CertTypes
from tests import ApiTestCase, betamaxed


class CreateTestCase(ApiTestCase):

    @betamaxed
    def test_create_with_minimal_parameters(self):
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
        order_id = self.api.ssl.create(product_id=CertTypes.COMODO_ESSENTIALSSL.product_id,
                                       period=1, csr=csr, software_id='linux',
                                       organization_handle='YN000088-NL',
                                       approver_email='hostmaster@example.com')
        self.assertIsInstance(order_id, int)
        self.assertGreater(order_id, 0)

    @betamaxed
    def test_create_with_all_parameters(self):
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
        order_id = self.api.ssl.create(product_id=CertTypes.COMODO_ESSENTIALSSL.product_id,
                                       period=1, csr=csr, software_id='linux',
                                       organization_handle='YN000088-NL',
                                       approver_email='hostmaster@example.com',
                                       signature_hash_algorithm='sha2',
                                       domain_validation_methods={'example.com': 'dns'},
                                       technical_handle='YN000088-NL')
        self.assertIsInstance(order_id, int)
        self.assertGreater(order_id, 0)


class DecodeCsrTestCase(ApiTestCase):

    @betamaxed
    def test_decode_valid_csr(self):
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

        result = self.api.ssl.decode_csr(csr)
        self.assertEqual(result['publicKey']['bits'], 2048)
        self.assertEqual(result['publicKey']['key'], key)
        self.assertEqual(result['subject']['commonName'], 'example.com')
        self.assertEqual(result['subject']['organization'], 'Default Company Ltd')
        self.assertEqual(result['subject']['unit'], '')
        self.assertEqual(result['subject']['locality'], 'Default City')
        self.assertEqual(result['subject']['state'], '')
        self.assertEqual(result['subject']['country'], 'NL')
        self.assertEqual(result['subject']['email'], '')
        self.assertEqual(result['signatureHashAlgorithm'], 'sha256WithRSAEncryption')
        self.assertEqual(result['subjectAlternativeName'], '')
        self.assertEqual(result['domainNamesCount'], 1)
