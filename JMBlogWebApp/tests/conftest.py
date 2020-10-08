from app import app
import pytest

@pytest.fixture
def my_app():
    response = app.test_client()
    return response