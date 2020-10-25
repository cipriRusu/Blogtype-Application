from repository.posts_repository import PostsRepository

class PostsInMemoryRepository(PostsRepository):
    def __init__(self, db):
        self._db = db

    def get_parameters(self, **conn):
        pass

    def __iter__(self):
        for element in self._db:
            yield element

    def add_post(self, item):
        self._db.append(item)

    def update_post(self, item):
        self._db.remove(item)
        self._db.append(item)

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
