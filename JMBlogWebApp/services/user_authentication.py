from flask import session
from services.password_hasher import PasswordHasher
from models.user import User

class UserAuthentication():
    def __init__(self, users_db):
        self._db = users_db
        self._username = None
        self._password_hash = None
        self._found_user = None
        self.flag_unset_password = False

    def user_login(self, form_user, form_pass):
        self._username = form_user
        self._password_hash = PasswordHasher().get_hash(form_pass)
        self._found_user = self._db.get_by_name(self._username)

        if (self._found_user is not None) and (self._found_user.user_password is None):
            self.flag_unset_password = True
            session['logged_name'] = self._found_user.user_name
            session['logged_id'] = self._found_user.user_id

        if (self._found_user is not None) and (self._password_hash ==
                                               self._found_user.user_password):
            session['logged_name'] = self._found_user.user_name
            session['logged_id'] = self._found_user.user_id
            return True
        return False

    def login_update(self, update_user):
        if session['logged_name'] is not 'admin':
            session['logged_name'] = update_user.user_name
            session['logged_id'] = update_user.user_id

    @classmethod
    def user_logout(cls):
        session.pop('logged_name', None)
        session.pop('logged_id', None)
