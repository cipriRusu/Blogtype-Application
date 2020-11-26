import hashlib

class PasswordHasher:
    def __init__(self):
        pass

    @classmethod
    def get_hash(cls, plain_text):
        if not plain_text:
            return ''
        return hashlib.sha256(plain_text.encode('utf-8')).hexdigest()
