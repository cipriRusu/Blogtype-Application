from models.user import User
from repository.users_repository import UsersRepository

class UsersDBRepository(UsersRepository):
    def __init__(self, db):
        self._db = db

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
        self._db.create_connection()
        all_elements = []
        query_result = self._db.execute('SELECT * FROM users')

        for user in query_result.fetchall():
            current_user = User(user[1], user[2], user[3])
            current_user.user_id = user[0]
            current_user.user_timestamp.creation_time = user[4]
            current_user.user_timestamp.edit_time = user[5]
            all_elements.append(current_user)

        self._db.close_connection()
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

    def remove_user(self, user_id):
        self._db.create_connection()
        self._db.execute("DELETE FROM users WHERE user_id=%s;", (str(user_id),))
        self._db.close_connection()
