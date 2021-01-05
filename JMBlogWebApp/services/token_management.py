import datetime
import jwt
from flask import current_app

class TokenHandler():
    def __init__(self):
        pass

    @classmethod
    def create_token(cls, user):
        token = jwt.encode({'user_id': user.user_id.hex,
                            'user_name': user.user_name,
                            'user_password': user.user_password,
                            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},
                           current_app.config['LOGIN_KEY'])
        return token
