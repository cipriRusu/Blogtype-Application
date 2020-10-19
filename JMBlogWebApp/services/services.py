from repository.posts_db_repository import PostsDBRepository as db
from repository.posts_in_memory_repository import PostsInMemoryRepository as test_db
from repository.in_memory_data import in_memory_db as test_data

class Services:
    def __init__(self):
        pass

    def get_service(self, service_name):
        if service_name == 'database':
            return db()
        if service_name == 'test':
            return test_db(test_data)
