from mock_db import MockDatabase

class BaseRepository:
    def __init__(self):
        self._db = MockDatabase()

    def add_post(self, item):
        self._db.add_post(item)

    def get_all(self):
        return iter(self._db)

    def get_by_id(self, index):
        return self._db.get_by_index(index)

    def remove(self, index):
        return self._db.remove(index)
