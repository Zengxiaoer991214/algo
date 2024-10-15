import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AesEncryptionUtil:
    @staticmethod
    def aes_encode(aes_key, source):
        if not source or source.isspace():
            return ""

        try:
            input_data = source.encode('utf-8')
            encrypted_data = AesEncryptionUtil.encrypt(input_data, aes_key)
            return base64.b64encode(encrypted_data).decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
            return ""

    @staticmethod
    def get_key_by_aes(aes_key, source):
        if not aes_key or not source:
            return ""

        try:
            input_data = base64.b64decode(source)
            output_data = AesEncryptionUtil.decrypt(input_data, aes_key)
            return output_data.decode('utf-8')
        except Exception as e:
            print(f"Decryption error: {e}")
            raise RuntimeError("error.aes_decrypt_error")

    @staticmethod
    def encrypt(data, aes_key):
        key_bytes = aes_key.encode('utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv=key_bytes)
        padded_data = pad(data, AES.block_size)
        return cipher.encrypt(padded_data)

    @staticmethod
    def decrypt(data, aes_key):
        key_bytes = aes_key.encode('utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv=key_bytes)
        decrypted_data = cipher.decrypt(data)
        return unpad(decrypted_data, AES.block_size)

    @staticmethod
    def get_key_by_aes_default(source):
        return AesEncryptionUtil.get_key_by_aes("0123456789123456", source)

    @staticmethod
    def aes_encode_default(source):
        return AesEncryptionUtil.aes_encode("0123456789123456", source)

    @staticmethod
    def get_aes_encryption_str(key, source):
        return AesEncryptionUtil.aes_encode(AesEncryptionUtil.get_key_by_aes(key, source))


if __name__ == '__main__':
    encrypted = AesEncryptionUtil.aes_encode_default("Hello World!")
    decrypted = AesEncryptionUtil.get_key_by_aes_default(encrypted)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
