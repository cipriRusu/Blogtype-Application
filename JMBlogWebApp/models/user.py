import uuid
from models.timestamp import TimeStamp
from services.password_hasher import PasswordHasher

class User:
    def __init__(self, user_name, user_email, user_password):
        self.user_id = uuid.uuid4()
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = PasswordHasher().get_hash(user_password)
        self.user_timestamp = TimeStamp()

    def update(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = (PasswordHasher().get_hash(user_password)
                              if user_password
                              else self.user_password)

        self.user_timestamp.on_edit()
