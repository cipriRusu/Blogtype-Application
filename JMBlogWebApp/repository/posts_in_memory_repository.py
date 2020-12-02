from repository.in_memory_data import in_memory_users
from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self, db):
        self._db = db

    def __iter__(self):
        for element in self._db:
            yield element

    def add_post(self, item):
        for user in in_memory_users:
            if user.user_id == item.author:
                item.author = user.user_name
        self._db.append(item)

    def update_post(self, item):
        for user in in_memory_users:
            if user.user_id == item.author:
                if user.user_name != 'admin':
                    item.author = user.user_name

                if user.user_name == 'admin':
                    item.author = item.older_author

    def get_by_id(self, index):
        for element in self._db:
            if element.post_id == index:
                return element
        raise Exception("no element found!")

    def get_all(self):
        return self._db

    def remove(self, index):
        for element in self._db:
            if element.post_id == index:
                self._db.remove(element)
