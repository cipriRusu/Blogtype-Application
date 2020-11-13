from services.password_hasher import PasswordHasher

class UserAuthentication:
    def __init__(self, connection):
        self._conn = connection
        self._username = None
        self._password_hash = None
        self._query_result = None

    def get_credentials(self, form_user, form_pass):
        self._username = form_user
        self._password_hash = PasswordHasher().get_hash(form_pass)

    def is_login_valid(self):
        self._conn.create_connection()
        self._query_result = self._conn.execute("SELECT EXISTS\
                                                (SELECT * FROM\
                                                 users WHERE user_name =%s\
                                                 AND user_password =%s)::BOOL",
                                                (self._username,
                                                 self._password_hash))
        return self._query_result.fetchone()[0]
