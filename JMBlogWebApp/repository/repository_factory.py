from repository.data_source_type import DataSourceType
from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.posts_db_repository import PostsDBRepository

class RepositoryFactory:
    def __init__(self, sourceType):
        self.sourceType = sourceType
    def get_source(self):
        if self.sourceType == DataSourceType.LocalSource:
            return PostsInMemoryRepository()
        elif self.sourceType == DataSourceType.DatabaseSource:
            return PostsDBRepository()
        else:
            return Exception('Data source unknown')
