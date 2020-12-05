from repository.in_memory_data import in_memory_posts
from repository.users_repository import UsersRepository

class UsersInMemoryRepository(UsersRepository):
    def __init__(self, db):
        self._db = db

    def __iter__(self):
        for element in self._db:
            yield element

    def add_user(self, user):
        self._db.append(user)

    def update_user(self, user):
        self._db.remove(user)
        self._db.append(user)

    def get_users(self):
        return self._db

    def get_user_by_id(self, user_id):
        for element in self._db:
            if element.user_id == user_id:
                return element
        raise Exception('No user found in current repository')

    def get_by_name(self, username):
        for element in self._db:
            if element.user_name == username:
                return element
        return None

    def remove_user(self, user_id):
        for element in self._db:
            if element.user_id == user_id:
                self._db.remove(element)
                for post in in_memory_posts:
                    if post.author == element.user_name:
                        in_memory_posts.remove(post)
