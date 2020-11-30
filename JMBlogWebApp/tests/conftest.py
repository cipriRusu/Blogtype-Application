import pytest
from mock import patch
from app import app
from services.services import Services

Services.IS_TEST = True

@pytest.fixture
def configured_app(scope='function'):
    with patch('setup.db_config.DbConfig.is_configured', return_value=True):
        with patch('setup.db_setup.DbSetup.is_db_outdated', return_value=False):
            response_from = app.test_client()
            app.config['TEST'] = True
            yield response_from

@pytest.fixture
def unconfigured_app():
    with patch('setup.db_config.DbConfig.is_configured', return_value=False):
        response_from = app.test_client()
        app.config['TEST'] = True
        yield response_from
