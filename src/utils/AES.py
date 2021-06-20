import pyaes
import hashlib
from base64 import b64encode, b64decode


class AESCipher:
    """
    This class defines the functions to encrypt and decrypt messages with AES
    """

    def __init__(self, key, iv):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()
        self.iv = iv

    def encrypt(self, pt):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        ct = b64encode(aes.encrypt(pt))
        return ct

    def decrypt(self, ct):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        pt = aes.decrypt(b64decode(ct))
        return pt
