import base64
import json

def test_get_valid_code_for_valid_login(configured_app):
    credentials = base64.b64encode(b"admin:adminpass").decode('utf-8')
    login_token_code = (configured_app.post('/api/login',
                                            headers={"authorization": "Basic " + credentials})
                        .status_code)
    assert login_token_code == 200

def test_get_valid_code_for_invalid_login(configured_app):
    credentials = base64.b64encode(b"invalid:invalid").decode('utf-8')
    login_token_code = (configured_app.post('/api/login',
                                            headers={"authorization": "Basic " + credentials})
                        .status_code)
    assert login_token_code == 403

def test_get_all_posts_route(configured_app):
    response = configured_app.get('/api/posts', follow_redirects=True).data

    expected_data = "f9c3a576-28bc-4b63-931d-04d6488d2f0d"
    other_expected_data = "Lorem Ipsum is simply dummy"

    assert expected_data.encode('utf-8') and other_expected_data.encode('utf-8') in response

def test_get_post_returns_specific_resource(configured_app):
    response = configured_app.get('/api/posts/be3e1383-d296-4956-85d2-d0da74c78531',
                                  follow_redirects=True).data

    expeted_data = "\"title\": \"EleventhTitle\""

    assert expeted_data.encode('utf-8') in response

def test_get_post_returns_error_for_invalid_resource_code(configured_app):
    response = configured_app.get('/api/posts/invalid',
                                  follow_redirects=True).status_code
    assert response == 404

def test_get_post_returns_error_for_valid_unexistent_resource_code(configured_app):
    response = configured_app.get('/api/posts/66b0ad30-3885-4448-b54b-f73f6376d5e5',
                                  follow_redirects=True).status_code
    assert response == 404

def test_post_remove_returns_error_code_if_unauthenticated(configured_app):
    response = configured_app.get('/api/posts/remove/be3e1383-d296-4956-85d2-d0da74c78531',
                                  follow_redirects=True).status_code
    assert response == 403

def test_post_remove_returns_error_message_if_unauthenticated(configured_app):
    response = configured_app.get('/api/posts/remove/be3e1383-d296-4956-85d2-d0da74c78531',
                                  follow_redirects=True).data
    expected_output = "\"message\": \"Post removing failed!\""
    assert expected_output.encode('utf-8') in response

def test_post_remove_works_normally_with_valid_authentication(configured_app):
    credentials = base64.b64encode(b"admin:adminpass").decode('utf-8')

    login_token = (json.loads(configured_app.post('/api/login',
                                                  headers={"authorization": "Basic " + credentials})
                              .data).get('token'))

    post_remove = configured_app.get('/api/posts/remove/be3e1383-d296-4956-85d2-d0da74c78531',
                                     headers={"authorization": "Bearer " + login_token}).data

    assert "Post was deleted successfully!".encode('utf-8') in post_remove

def test_post_remove_fails_with_invalid_authentication(configured_app):
    credentials = base64.b64encode(b"FirstAuthor:fpass").decode('utf-8')

    login_token = (json.loads(configured_app.post('/api/login',
                                                  headers={"authorization": "Basic " + credentials})
                              .data).get('token'))

    post_remove = configured_app.get('/api/posts/remove/be3e1383-d296-4956-85d2-d0da74c78531',
                                     headers={"authorization": "Bearer " + login_token}).data

    assert "Unauthorized operation".encode('utf-8') in post_remove
