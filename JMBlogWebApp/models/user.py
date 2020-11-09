import uuid
from models.timestamp import TimeStamp

class User:
    def __init__(self, user_name, user_email, user_password):
        self.user_id = uuid.uuid4()
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password #temp: to hash
        self.user_timestamp = TimeStamp()

    def update(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.stamp.on_edit()