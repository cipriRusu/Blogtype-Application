import pytest
from app import app
from views import post_manager
from repository.repository_factory import RepositoryFactory
from repository.data_source_type import DataSourceType

class TestPostManagerClass:
    def test_first(self):
        post_manager.test_mode = True
        res = app.route('/posts/')

if __name__ == '__main__':
    pytest.main()
