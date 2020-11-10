import uuid
from models.timestamp import TimeStamp
from models.password_hasher import PasswordHasher

class User:
    def __init__(self, user_name, user_email, user_password):
        self.user_id = uuid.uuid4()
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = PasswordHasher().GetHash(user_password)
        self.user_timestamp = TimeStamp()

    def update(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_timestamp.on_edit()
