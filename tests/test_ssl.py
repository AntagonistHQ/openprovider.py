from textwrap import dedent
from tests import ApiTestCase, betamaxed


class DomainTestCase(ApiTestCase):

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
        -----END CERTIFICATE REQUEST-----""")
        order_id = self.api.ssl.create(product_id=5, period=1, csr=csr, software_id='linux',
                organization_handle='YN000088-NL', approver_email='hostmaster@example.com')
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
        -----END CERTIFICATE REQUEST-----""")
        order_id = self.api.ssl.create(product_id=5, period=1, csr=csr, software_id='linux',
                organization_handle='YN000088-NL', approver_email='hostmaster@example.com',
                signature_hash_algorithm='sha2')
        self.assertIsInstance(order_id, int)
        self.assertGreater(order_id, 0)
