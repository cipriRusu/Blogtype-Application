import pytest
from app import app
from views import post_manager

class TestPostManagerClass:
    def test_post_manager_basic_response(self):
        post_manager.TEST_MODE = True
        app.register_blueprint(post_manager.post_manager)
        result = app.test_client()
        response = result.get('/posts/')
        assert response.status == '200 OK'

    def test_posts_manager_static_content_response(self):
        post_manager.TEST_MODE = True
        app.register_blueprint(post_manager.post_manager)
        result = app.test_client()
        response = result.get('/posts/')
        assert b"Blog App" in response.data
