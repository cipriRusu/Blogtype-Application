import hashlib

class PasswordHasher:
    def __init__(self):
        pass

    def get_hash(self, plain_text):
        return hashlib.sha256(plain_text.encode('utf-8')).hexdigest()
