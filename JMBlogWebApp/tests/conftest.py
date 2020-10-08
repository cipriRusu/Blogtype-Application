import pytest
from app import app
from repository.repository_factory import RepositoryFactory

RepositoryFactory.IS_TEST = True

@pytest.fixture
def current_app():
    response_from = app.test_client()
    return response_from
