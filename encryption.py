import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AESCipher:
    def __init__(self, key_hex: str):
        """
        key_hex: AES key stored as hex string in .env (64 chars for AES-256)
        """
        self.key = bytes.fromhex(key_hex.strip())

        # Validate key length (must be 16/24/32 bytes)
        if len(self.key) not in (16, 24, 32):
            raise ValueError(f"Invalid AES key length: {len(self.key)} bytes")

    def encrypt(self, raw_data: bytes) -> bytes:
        """Encrypts raw bytes using AES-CFB."""
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        encrypted = iv + cipher.encrypt(raw_data)
        return encrypted

    def decrypt(self, enc_data: bytes) -> bytes:
        """Decrypts encrypted bytes using AES-CFB."""
        iv = enc_data[:16]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        decrypted = cipher.decrypt(enc_data[16:])
        return decrypted
