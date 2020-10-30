from setup import services_listing as service
from setup.config import Config
from setup.db_connect  import DbConnect
from setup.db_setup import DbSetup
from repository.posts_db_repository import PostsDBRepository
from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.in_memory_data import in_memory_db as test_data

class Services():
    IS_TEST = False
    def __init__(self):
        pass

    configuration = Config()
    connection = DbConnect(configuration)
    posts_repository = PostsDBRepository(connection)
    test_repository = PostsInMemoryRepository(test_data)

    test = {service.DATA_SOURCE: test_repository,
            service.CONFIGURE: configuration,
            service.CONNECT: connection,
            service.SETUP: DbSetup(configuration)}

    production = {service.DATA_SOURCE: posts_repository,
                  service.CONFIGURE: configuration,
                  service.CONNECT: connection,
                  service.SETUP: DbSetup(configuration)}

    @classmethod
    def get_service(cls, service_name):
        return (Services.test[service_name]
                if Services.IS_TEST else Services.production[service_name])
