class Pagination():
    POSTS_LIMIT = 5
    def __init__(self, db, name_filter, page_filter):
        self._db = db
        self._name_filter = name_filter
        self._page_filter = page_filter
        self._contains = True

    def can_next(self):
        if self._contains:
            return True
        return False

    def can_previous(self):
        if self._page_filter - 1 >= 0:
            return True
        return False

    def get_previous(self):
        previous = self._page_filter - 1
        return previous

    def get_next(self):
        next_index = self._page_filter + 1
        return next_index

    def get_page(self):
        current_posts = self._db.get_all(filter_by=self._name_filter)
        current_posts.reverse()
        returned = (current_posts[self._page_filter * Pagination.POSTS_LIMIT:]
                                 [0:Pagination.POSTS_LIMIT])
        if not returned:
            self._contains = False
        return returned
