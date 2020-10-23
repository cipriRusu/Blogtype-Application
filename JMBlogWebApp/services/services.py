from setup.config import Config as config
from setup.db_connect  import DbConnect as connect
from setup.db_setup import DbSetup as setup
from repository.posts_db_repository import PostsDBRepository as db
from repository.posts_in_memory_repository import PostsInMemoryRepository as test_db
from repository.in_memory_data import in_memory_db as test_data

class Services:
    IS_TEST = False
    def __init__(self):
        pass

    def get_service(self, service_name):
        if service_name == 'data_source':
            return test_db(test_data) if Services.IS_TEST else db()

        if service_name == 'config':
            return config()

        if service_name == 'connect':
            setup(**config().from_file('db_connection')).create_database()
            connect(True, **config().from_file('db_connection'))
