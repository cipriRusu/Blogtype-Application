import pytest
from app import app
from services.services import Services

Services.IS_TEST = True

@pytest.fixture
def current_app():
    response_from = app.test_client()
    app.config['TEST'] = True
    return response_from
