from repository.data_source_type import DataSourceType
from repository.posts_in_memory_repository import PostsInMemoryRepository

class RepositoryFactory:
    def __init__(self, sourceType):
        self.sourceType = sourceType
    def GetSource(self):
        if self.sourceType == DataSourceType.LocalSource:
            return PostsInMemoryRepository()
        elif self.sourceType == DataSourceType.DatabaseSource:
            pass #TODO: return DatabaseRepository when implemented
        else:
            return Exception('Data source unknown')
