from models.user import User
from repository.users_repository import UsersRepository

class UsersInMemoryRepository(UsersRepository):
    def __init__(self, db):
        self._db = db

    def __iter__(self):
        for element in self._db:
            yield element

    def add_user(self, user):
        self._db.append(item)

    def update_user(self, user):
        self._db.remove(item)
        self._db.append(item)

    def get_users(self):
        return self._db

    def get_user_by_id(self, user_id):
        for element in self._db:
            if element.user_id == user_id:
                return element

    def remove_user(self, user_id):
        for element in self._db:
            if element.post_id == index:
                self._db.remove(element)
