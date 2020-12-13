from setup import services_listing as service
from setup.db_config import DbConfig
from setup.db_connect import DbConnect
from setup.db_setup import DbSetup
from repository.posts_db_repository import PostsDBRepository
from repository.users_db_repository import UsersDBRepository
from repository.posts_in_memory_repository import PostsInMemoryRepository
from repository.users_in_memory_repository import UsersInMemoryRepository
from repository.in_memory_data import in_memory_posts as test_data_posts
from repository.in_memory_data import in_memory_users as test_data_users
from services.user_authentication import UserAuthentication
from services.pagination_factory import PaginationFactory
from services.sqa_engine import SQAEngine

class Services():
    IS_TEST = False
    def __init__(self):
        pass

    db_configuration = DbConfig()
    connection = DbConnect(db_configuration)
    setup = DbSetup(connection)
    test_users_repository = UsersInMemoryRepository(test_data_users)
    test_posts_repository = PostsInMemoryRepository(test_data_posts, test_users_repository)
    sqa_engine = SQAEngine(db_configuration)
    posts_repository = PostsDBRepository(sqa_engine)
    users_repository = UsersDBRepository(sqa_engine)
    database_login = UserAuthentication(users_repository)
    test_login = UserAuthentication(test_users_repository)
    pagination_factory = PaginationFactory()

    test = {service.DB_CONFIGURATION: db_configuration,
            service.DATA_SOURCE_POSTS: test_posts_repository,
            service.DATA_SOURCE_USERS: test_users_repository,
            service.CONNECT: connection,
            service.SETUP: setup,
            service.USER_LOGIN: test_login,
            service.PAGINATION_FACTORY: pagination_factory}

    production = {service.DB_CONFIGURATION: db_configuration,
                  service.DATA_SOURCE_POSTS: posts_repository,
                  service.DATA_SOURCE_USERS: users_repository,
                  service.CONNECT: connection,
                  service.SETUP: setup,
                  service.USER_LOGIN: database_login,
                  service.PAGINATION_FACTORY: pagination_factory}

    @classmethod
    def is_service(cls, service_name):
        all_services = {k:v for (k, v) in service.__dict__.items() if not k.startswith("_")}
        return service_name in all_services.values()

    @classmethod
    def get_service(cls, service_name):
        return (Services.test[service_name]
                if Services.IS_TEST else Services.production[service_name])
