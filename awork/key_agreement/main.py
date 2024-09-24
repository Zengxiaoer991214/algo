from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import binascii


def get_key_agreement(digital_signature):
    try:
        csr_bytes = binascii.unhexlify(digital_signature)

        csr = x509.load_der_x509_csr(csr_bytes, default_backend())

        public_key = csr.public_key()

        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint
        )

        return byte_array_to_hex_string(public_key_bytes)
    except Exception as e:
        print(f"Error parsing digital signature: {e}")
        return None


def byte_array_to_hex_string(public_key_bytes):
    return public_key_bytes.hex().upper()


def hex_string_to_byte_array(hex_string):
    return bytes.fromhex(hex_string)


if __name__ == '__main__':
    digital_signature = "3081F330819B020100301B3119301706035504030C10343834433539303030324641463535333059301306072A8648CE3D020106082A8648CE3D03010703420004C3CCF6A388EA8CCB6D557E65C9347D08E8DED154D46FE377EBDA72294ED5A34E675AFBBB1C77A9FDB483A21BCEC529A8EE0D09295BE6E4D92DF959043218DCF2A01E301C06092A864886F70D01090E310F300D300B0603551D0F040403020780300A06082A8648CE3D040302034700304402207B3B2234AD63DCFA58E2BD4C4D814D9EE1F7D931A1E3C426792D4F07F58798C40220944810C5F8B3023840750C997003163B6CB7C870AD0FAD722CC746AEAE2AEF40"
    print(get_key_agreement(digital_signature))

