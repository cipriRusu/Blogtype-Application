def test_redirects_user_manager(unconfigured_app):
    response = unconfigured_app.get('/users/').status_code
    assert response == 302
