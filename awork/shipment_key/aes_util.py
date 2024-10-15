import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


class AesUtil:
    AES_KEY_METHOD = 'AES'
    IVS_HEX = '00000000000000000000000000000000'

    @staticmethod
    def decrypt_aes(aes_key_hex, source_base64, ivs_hex=IVS_HEX):
        if not aes_key_hex or not source_base64:
            return ""

        try:
            aes_key = bytes.fromhex(aes_key_hex)
            iv = bytes.fromhex(ivs_hex)
            cipher = AES.new(aes_key, AES.MODE_CBC, iv)
            encrypted_bytes = base64.b64decode(source_base64)
            trimmed_encrypted = encrypted_bytes[16:]
            decrypted_bytes = cipher.decrypt(trimmed_encrypted)
            return AesUtil.byte2string(unpad(decrypted_bytes, AES.block_size))

        except Exception as e:
            print(f"AES Decrypt Error: {e}")
            raise RuntimeError("Aes Decrypt Error")

    @staticmethod
    def byte2string(byte_array):
        return ''.join(f"{byte:02X}" for byte in byte_array)


if __name__ == '__main__':
    toAscii = '4543344336423446463541373335303043344332344341323036464436304241'
    res = AesUtil.decrypt_aes(toAscii, r'AAAAAAAAAAAAAAAAAAAAAPXVHdu/ol8kM0ixzOwDZH9Mq7+07KRkyr48mLC67/EV')
    print(res)

