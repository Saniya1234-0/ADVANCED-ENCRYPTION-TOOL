import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class VaultEngine:
    def __init__(self, password: str):
        self.password = password.encode()

    def _get_key(self, salt: bytes):
        # Scrypt makes the password "expensive" to crack for hackers
        kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
        return kdf.derive(self.password)

    def encrypt(self, file_path):
        salt = os.urandom(16)
        nonce = os.urandom(12) # Unique number for this specific encryption
        key = self._get_key(salt)
        aesgcm = AESGCM(key)

        with open(file_path, 'rb') as f:
            data = f.read()

        ciphertext = aesgcm.encrypt(nonce, data, None)
        
        # Save salt + nonce + ciphertext into a new .enc file
        with open(file_path + ".enc", 'wb') as f:
            f.write(salt + nonce + ciphertext)

    def decrypt(self, file_path):
        with open(file_path, 'rb') as f:
            raw = f.read()

        # Extract the metadata we stored at the beginning
        salt, nonce, ciphertext = raw[:16], raw[16:28], raw[28:]
        key = self._get_key(salt)
        aesgcm = AESGCM(key)

        try:
            return aesgcm.decrypt(nonce, ciphertext, None)
        except Exception:
            return None # Returns None if password is wrong