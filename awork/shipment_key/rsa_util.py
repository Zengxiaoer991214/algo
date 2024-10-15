import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


class RSADecryptError(Exception):
    pass


class RsaUtil:
    @staticmethod
    def _decrypt_plain(encoded_str: str, private_key_pem: str, algorithm: str = 'RSA') -> str:
        if not encoded_str or encoded_str.isspace():
            return None

        try:
            # Decode the base64 encoded string
            input_bytes = base64.b64decode(encoded_str)

            # Load the private key
            private_key = RSA.import_key(private_key_pem)

            # Decrypt with RSA
            cipher = PKCS1_v1_5.new(private_key)
            decrypted_data = cipher.decrypt(input_bytes, None)

            if decrypted_data is None:
                raise ValueError("Decryption failed")

            return decrypted_data.decode('utf-8')

        except Exception as e:
            print(f"RSA decrypt error: {e}")
            raise RSADecryptError("error.rsa_decrypt_error")

    @staticmethod
    def decrypt(encoded_str: str, private_key_pem: str) -> str:
        return RsaUtil._decrypt_plain(encoded_str, private_key_pem, 'RSA')

    @staticmethod
    def convert_to_ascii(string: str):
        if not string or string.isspace():
            return None
        return ''.join(format(ord(c), 'x') for c in string)


if __name__ == '__main__':
    aes_key = (r'fW2Fd2fTvWUmRTvCZ7djHbJeS6INnU5b8Sj6waoj1cofG9j+GhIjjk34JjfnEm9pIh8EDlmDrMWNhUbH7b2fBumF+2M'
               r'/EzV2qvjSSqnvDnLIP2A9QjpiQQk6whdRwxCfNh0Ju7e4xMn4rsEdxRKuQAnSiMDJp1B3vsTqp+dYt4v3V6ZoL2XU3Pv9yOgs'
               r'+fw34aYk3SMMBHXBUBrgDuyJDMi22AAgh+lX9f3x2dEJXB8PvNQlXnBn6SDPnkTY1t+gWXfqN07Mz6MTKPdlDzN0JaIAzXi'
               r'/9fpH3Yqv/c2BeBfZ31NN9SyYlzn4Dn1udzYXHRqEGuX0h5m9yEuJS9Lexg==')
    private_key = '''-----BEGIN PRIVATE KEY-----
            MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCqJoxHPWeSCxQb
            FBwp18NWAFkZ5OqZUdI4zlCZKczBqH6sZeCok8BRwg5iISzFvRlbOXbE0n218meQ
            NdpOXJo4NYLcSPhtRWCBs1Wc4z+zGD0YuAND1aMlSKp+4eVf7Rt+uYeVN2kV1+mr
            hDJuewufOYeJ/RoiGWBmlX7sV9gQ6G22Uhl5IHxfGRje/Noh+dMcetSdPKLofj0U
            kxeeOO4bUUyHsZprBZT14a2CXJ9b/ZUrGsCFXOOIu0Y9UZolXLkrW71PpaPjVLFw
            pxWIlObqWav8YI/CO5zwSQsG2VmK9wZ4jourkxH0kfchwOfYOzj05COnrQ2Cn2Uo
            pLS8WDfXAgMBAAECggEAL9ep7ugVpKtnyltjteI8wwRTCWRkEJtAlIdygzaNI9DY
            WWpF+rCczYBWogH5AFq09AEa46nZ/hx8QUDbMth35qEpO/5ql/L/eUivJG+DfDyv
            BTHMfTjnaDbf9dBXuhrF9eJ9/Jd5fVJaGkeQFJ+Ve35mHYck33yqLf4QE615i/sR
            YpVy7o5cNpETR9lYsTtBEyyEVC05BkwocxVyWkrLnwzS7PMllTvUI9+ZDq//CjOX
            9zV/BriVOTLDng7K8b+Gui8v2NdFtRLBTncRplKcHFQ430hx1P4FQ7wuJ/ZeyFLt
            /4/cdMiGATRlzpVjKVuQFTrvbeWazYeG1z3vLSoIoQKBgQDV8y66ENPQGC9N+Yw7
            Yfar0YT5Pgf3VgxUo0D66mYRcrhCH3nGvQCXPq3pM/vdtADKPlrgzWitnz7cK0bq
            aRutSIx16oJxVWkXOHeaFcgCwRq1el5+pLDeazZPX/2f5iavTAMInBVIC4dacJOc
            q5MoqIh/6GWCMn+LCfxVc7nvIQKBgQDLl52v4qUPEOcrRmY6Zehg+XziBgtb1IAN
            yCDLn69MhXjRXli69AKRkYCQdpFMxU/tv6C+tuWIv3DxHqvLky6VfHBMA4ysh97p
            2poTeujre7Lu0YJagJM8XAd5jqoej8OakMljTsVfI1W2rYjRzRagTvu9L7A6CMo4
            yPPQu82f9wKBgDY0cnY5pTBnsDR1MQ4qd7B4WNQ83w/PATjAU8o+cLWi9wPprZSo
            denbu3wF653z6O9UdPnXkNnMKsTlQgZJsvVoGA4X6AyGsyVq7QJg2le4TOgFpMM5
            PoZba1sY2s0UJmDrRSl9QfcK1LQZKYzb+2Clsk+VtYITATVcxk1wEH+BAoGBAI19
            Xx9fWerwileu41jufeL3QG0sWjSFqEDrtq8M2R1LHT4UXYIAFtDn1/uOC0jZT8Uh
            CivAnCC/O1S3RhmCvjsxcjHBvcAh5S+MtsuW/cy5+Q60F+2hsbGfG6rFFUGMFBqV
            SQB1PAH0YptEWvPDnlfmzFkcjVKnzTJNpfSIsEzdAoGBAM9bwUm8gK73HNDi+wLY
            QltqBLjJlPf4ENqZOYVkCKcjoBUPpidVFeZfGXaTLOVQDqfF+fYZ9tB8UHPGMWhh
            ytfFVfDJs0Bzj0rxZpdaKRPRhOJFuKALmaHEUipSqNkZgD8wkmI8u8OuEwN1Wt0S
            biUvcYxDboqklzREtdKKz0mN
            -----END PRIVATE KEY-----'''
    print(RsaUtil.decrypt(aes_key, private_key))
    print(RsaUtil.convert_to_ascii(RsaUtil.decrypt(aes_key, private_key)))
