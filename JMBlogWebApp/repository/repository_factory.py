from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.posts_db_repository import PostsDBRepository
from repository.in_memory_data import db

class RepositoryFactory:
    IS_TEST = True
    @staticmethod
    def get_source():
        if RepositoryFactory.IS_TEST:
            return PostsInMemoryRepository(db)
        if not RepositoryFactory.IS_TEST:
            return PostsDBRepository()
        return Exception('Data source unknown')
