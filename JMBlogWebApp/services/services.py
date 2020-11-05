from setup import services_listing as service
from setup.db_config import DbConfig
from setup.db_connect  import DbConnect
from setup.db_setup import DbSetup
from repository.posts_db_repository import PostsDBRepository
from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.in_memory_data import in_memory_db as test_data

class Services():
    IS_TEST = False
    def __init__(self):
        pass

    db_configuration = DbConfig()
    connection = DbConnect(db_configuration)
    setup = DbSetup(connection)
    posts_repository = PostsDBRepository(connection)
    test_repository = PostsInMemoryRepository(test_data)

    test = {service.DB_CONFIGURATION: db_configuration,
            service.DATA_SOURCE: test_repository,
            service.CONNECT: connection,
            service.SETUP: setup}

    production = {service.DB_CONFIGURATION: db_configuration,
                  service.DATA_SOURCE: posts_repository,
                  service.CONNECT: connection,
                  service.SETUP: setup}

    @classmethod
    def is_service(cls, service_name):
        all_services = {k:v for (k, v) in service.__dict__.items() if not k.startswith("_")}
        return service_name in all_services.values()

    @classmethod
    def get_service(cls, service_name):
        return (Services.test[service_name]
                if Services.IS_TEST else Services.production[service_name])
