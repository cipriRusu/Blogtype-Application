from models.user import User
from models.sqa_models.sqa_users import Users
from repository.users_repository import UsersRepository

class UsersDBRepository(UsersRepository):
    def __init__(self, db):
        self._db = db

    def __iter__(self):
        for element in self.get_users():
            yield element

    def add_user(self, user):
        self._db.create_connection()
        self._db.execute('INSERT INTO users\
                         (user_id,\
                          user_name,\
                          user_email,\
                          user_password,\
                          user_created_at,\
                          user_modified_at)\
                          VALUES(%s, %s, %s, %s, %s, %s)',
                         (str(user.user_id),
                          user.user_name,
                          user.user_email,
                          user.user_password,
                          user.user_timestamp.creation_time,
                          user.user_timestamp.edit_time))

        self._db.close_connection()

    def update_user(self, user):
        self._db.create_connection()
        self._db.execute("UPDATE users SET\
        user_name = %s,\
        user_email = %s,\
        user_password = %s,\
        user_created_at = %s,\
        user_modified_at = %s WHERE user_id = %s",
                         (user.user_name,
                          user.user_email,
                          user.user_password,
                          user.user_timestamp.creation_time,
                          user.user_timestamp.edit_time,
                          user.user_id))

    def get_users(self):
        all_elements = []
        self._db.start_session()

        session = self._db.get_session()

        for user in session.query(Users).all():
            current_user = User(user.user_name, user.user_email, user.user_password)
            current_user.user_id = user.user_id
            current_user.user_timestamp.creation_time = user.user_created_at
            current_user.user_timestamp.edit_time = user.user_modified_at
            all_elements.append(current_user)

        self._db.close_session()
        return all_elements

    def get_user_by_id(self, user_id):
        self._db.create_connection()
        query_result = self._db.execute('SELECT * FROM users where user_id=%s', (str(user_id),))

        query_output = query_result.fetchone()

        user = User(
            query_output[1],
            query_output[2],
            query_output[3])

        user.user_id = query_output[0]
        user.user_timestamp.creation_time = query_output[4]
        user.user_timestamp.edit_time = query_output[5]

        self._db.close_connection()
        return user

    def get_by_name(self, username):
        self._db.create_connection()
        query_result = self._db.execute("SELECT * FROM users WHERE user_name =%s", (username, ))

        query_output = query_result.fetchone()

        if query_output is not None:
            user = User(
                query_output[1],
                query_output[2],
                query_output[3])

            user.user_password = query_output[3]
            user.user_id = query_output[0]
            user.user_timestamp.creation_time = query_output[4]
            user.user_timestamp.edit_time = query_output[5]

        else:
            user = None

        self._db.close_connection()
        return user

    def remove_user(self, user_id):
        self._db.create_connection()
        self._db.execute("DELETE FROM users WHERE user_id=%s;", (str(user_id),))
        self._db.close_connection()
