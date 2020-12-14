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
        self._db.start_session()

        session = self._db.get_session()

        user_to_add = Users()

        user_to_add.user_id = (str(user.user_id))
        user_to_add.user_name = user.user_name
        user_to_add.user_email = user.user_email
        user_to_add.user_password = user.user_password
        user_to_add.user_created_at = user.user_timestamp.creation_time
        user_to_add.user_modified_at = user.user_timestamp.edit_time

        session.add(user_to_add)

        self._db.close_session()

    def update_user(self, user):
        self._db.start_session()

        session = self._db.get_session()

        session.query(Users).filter(Users.user_id == user.user_id).update({
            Users.user_name: user.user_name,
            Users.user_email: user.user_email,
            Users.user_password: user.user_password,
            Users.user_created_at: user.user_timestamp.creation_time,
            Users.user_modified_at: user.user_timestamp.edit_time})

        self._db.close_session()

    def get_users(self):
        all_elements = []
        self._db.start_session()

        session = self._db.get_session()

        for user in session.query(Users).all():
            current_user = User(user.user_name,
                                user.user_email,
                                user.user_password)

            current_user.user_id = user.user_id
            current_user.user_timestamp.creation_time = user.user_created_at
            current_user.user_timestamp.edit_time = user.user_modified_at

            all_elements.append(current_user)

        self._db.close_session()
        return all_elements

    def get_user_by_id(self, user_id):
        self._db.start_session()

        session = self._db.get_session()

        query_output = (session.query(Users)
                        .filter(Users.user_id == user_id.hex)
                        .first())

        if query_output is not None:
            user = User(query_output.user_name,
                        query_output.user_email,
                        query_output.user_password)

            user.user_password = query_output.user_password
            user.user_id = query_output.user_id
            user.user_timestamp.creation_time = query_output.user_created_at
            user.user_timestamp.edit_time = query_output.user_modified_at

            self._db.close_session()

            return user
        return None

    def get_by_name(self, username):
        self._db.start_session()

        session = self._db.get_session()

        query_output = (session.query(Users)
                        .filter(Users.user_name == username)
                        .first())

        if query_output is not None:
            user = User(query_output.user_name,
                        query_output.user_email,
                        query_output.user_password)

            user.user_password = query_output.user_password
            user.user_id = query_output.user_id
            user.user_timestamp.creation_time = query_output.user_created_at
            user.user_timestamp.edit_time = query_output.user_modified_at

            self._db.close_session()

            return user
        return None

    def remove_user(self, user_id):
        self._db.start_session()

        session = self._db.get_session()

        (session.query(Users)
         .filter(Users.user_id == user_id.hex)
         .delete(synchronize_session=False))

        self._db.close_session()
