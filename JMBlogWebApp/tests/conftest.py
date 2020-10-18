import pytest
from app import app

@pytest.fixture
def current_app():
    response_from = app.test_client()
    return response_from
