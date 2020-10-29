from setup import services_listing as service
from setup.config import Config as config
from setup.db_connect  import DbConnect as connect
from setup.db_setup import DbSetup as setup
from repository.posts_db_repository import PostsDBRepository as db
from repository.posts_in_memory_repository import PostsInMemoryRepository as test_db
from repository.in_memory_data import in_memory_db as test_data

class Services():
    IS_TEST = False
    def __init__(self):
        pass

    test = {service.DATA_SOURCE: test_db(test_data),
            service.CONFIGURE: config(),
            service.CONNECT: connect(config()),
            service.SETUP: setup(config())}


    production = {service.DATA_SOURCE: db(connect(config())),
               service.CONFIGURE: config(),
               service.CONNECT: connect(config()),
               service.SETUP: setup(config())}

    @classmethod
    def get_service(cls, service_name):
        return Services.test[service_name] if Services.IS_TEST else Services.production[service_name]
