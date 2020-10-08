from app import app
import pytest

@pytest.fixture
def current_app():
    response_from = app.test_client()
    return response_from