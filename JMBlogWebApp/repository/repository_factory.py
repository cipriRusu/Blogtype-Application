from repository.data_source_type import DataSourceType
from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.posts_db_repository import PostsDBRepository

class RepositoryFactory:
    def __init__(self, source_type):
        self.source_type = source_type
    def get_source(self):
        if self.source_type == DataSourceType.LocalSource:
            return PostsInMemoryRepository()
        elif self.source_type == DataSourceType.DatabaseSource:
            return PostsDBRepository()
        else:
            return Exception('Data source unknown')
