from flask import session
from services.password_hasher import PasswordHasher

class UserAuthentication():
    def __init__(self, users_db):
        self._db = users_db
        self._username = None
        self._password_hash = None
        self._found_user = None

    def user_login(self, form_user, form_pass):
        self._username = form_user
        self._password_hash = PasswordHasher().get_hash(form_pass)
        self._found_user = self._db.get_by_name_and_pass(self._username,
                                                         self._password_hash)

        if self._found_user is not None:
            session['logged_name'] = self._found_user.user_name
            session['logged_id'] = self._found_user.user_id
            return True
        return False
