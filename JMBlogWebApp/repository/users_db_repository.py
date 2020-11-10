from repository.users_repository import UsersRepository

class UsersDBRepository(UsersRepository):
    def __init__(self, db):
        self._db = db

    def add_user(self, user):
        pass

    def update_user(self, user):
        pass

    def get_users(self):
        pass

    def get_user_by_id(self, user_id):
        pass

    def remove_user(self, user_id):
        pass
