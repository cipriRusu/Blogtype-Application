from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.posts_db_repository import PostsDBRepository
from repository.in_memory_data import in_memory_db

class RepositoryFactory:
    IS_TEST = True
    @staticmethod
    def get_source():
        if RepositoryFactory.IS_TEST:
            return PostsInMemoryRepository(in_memory_db)
        if not RepositoryFactory.IS_TEST:
            return PostsDBRepository()
        return Exception('Data source unknown')
