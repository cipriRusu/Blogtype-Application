class Pagination():
    POSTS_LIMIT = 1
    def __init__(self, db):
        self._db = db
        self._size = self._db
        self._name_filter = 'None'
        self._current_page = 0

    def can_next(self):
        if self._current_page < len(self._db.get_all(filter_by=self._name_filter)
                                    [self._current_page * Pagination.POSTS_LIMIT:
                                     self._current_page + Pagination.POSTS_LIMIT]) + 1:
            return True
        return False

    def can_previous(self):
        if self._current_page - 1 >= 0:
            return True
        return False

    def get_previous(self):
        previous_page = self._current_page - 1
        return previous_page

    def get_next(self):
        next_page = self._current_page + 1
        return next_page

    def get_name_filter(self, name_filter):
        self._name_filter = name_filter

    def get_page_filter(self, page_filter):
        self._current_page = page_filter

    def get_current_page(self):
        return (self._db.get_all(filter_by=self._name_filter)
                [self._current_page * Pagination.POSTS_LIMIT:
                 self._current_page + Pagination.POSTS_LIMIT])
