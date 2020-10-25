from setup import services_listing as service
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

    services_container = {
        service.DATA_SOURCE: db(),
        service.CONFIGURE: config(),
        service.CONNECT: connect(),
        service.SETUP: setup()}

    test_container = {
        service.DATA_SOURCE: test_db(test_data),
        service.CONFIGURE: config(),
        service.CONNECT: connect(),
        service.SETUP: setup()}

    singletons = {}

    @classmethod
    def get_service(cls, service_name):
        if service_name not in Services.singletons:
            Services.singletons[service_name] = (Services.test_container[service_name]
                                                 if Services.IS_TEST
                                                 else Services.services_container[service_name])
            return Services.singletons[service_name]
        return Services.singletons[service_name]
