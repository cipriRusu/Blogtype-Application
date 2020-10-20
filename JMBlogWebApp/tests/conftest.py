import pytest
from app import app
from services.services import Services

@pytest.fixture
def current_app():
    app.config['DATA_SOURCE'] = Services().get_service('test')
    response_from = app.test_client()
    return response_from
