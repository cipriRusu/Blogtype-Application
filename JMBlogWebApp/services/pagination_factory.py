from services.pagination import Pagination

class PaginationFactory():
    def __init__(self):
        self._datasource = None
        self._name_filter = None
        self._page_filter = None

    def get_parameters(self, datasource, name_filter, page_filter):
        self._datasource = datasource

        self._name_filter = None if name_filter in (None, "None", '') else name_filter

        self._page_filter = (0 if page_filter in (None, "None", '')
                             else int(page_filter)
                             if page_filter.isnumeric() else 0)

    def get_pagination(self):
        return Pagination(self._datasource,
                          self._name_filter,
                          self._page_filter)
