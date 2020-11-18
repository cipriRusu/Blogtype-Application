def test_unlogged_basic_login(configured_app):
    current = configured_app.get('/authentication/login', follow_redirects=True).data
    assert b'Login' in current

def test_login_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}
    current = configured_app.post('/authentication/login', data=login_data,
                                  follow_redirects=True).data
    assert b'FirstTitle' in current

def test_redirect_after_correct_user_login(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}
    current = configured_app.post('/authentication/login', data=login_data,
                                  follow_redirects=True).data
    assert b'FirstTitle' in current

def test_redirect_after_incorrect_user_login(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "wrongpass"}
    current = configured_app.post('/authentication/login', data=login_data,
                                  follow_redirects=True).data
    assert b'Invalid login' in current
