class Pagination():
    POSTS_LIMIT = 5
    def __init__(self, db, name_filter, page_filter):
        self._db = db
        self._name_filter = name_filter
        self._page_filter = page_filter
        self.can_continue = True

    def can_next(self):
        if self.can_continue:
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
        all_posts = self._db.get_all(filter_by=self._name_filter)

        all_posts.reverse()

        posts_on_current_page = self.__extracted_posts(all_posts, self._page_filter)

        if not len(posts_on_current_page) >= Pagination.POSTS_LIMIT:
            self.can_continue = False

        if not self.__extracted_posts(all_posts, self._page_filter + 1):
            self.can_continue = False

        return posts_on_current_page

    @classmethod
    def __extracted_posts(cls, all_posts, page_index):
        return all_posts[page_index * Pagination.POSTS_LIMIT:][0:Pagination.POSTS_LIMIT]
