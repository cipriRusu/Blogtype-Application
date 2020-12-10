def test_unlogged_basic_login(configured_app):
    current = configured_app.get('/authentication/login', follow_redirects=True).data
    assert b'Login' in current

def test_login_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}
    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    after_login_page = configured_app.get('/posts/?Page=0').data
    assert b'SecondTitle' in after_login_page

def test_redirect_after_correct_user_login(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}
    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    after_login_page = configured_app.get('/posts/?Page=0').data
    assert b'SecondTitle' in after_login_page

def test_redirect_after_incorrect_user_login(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "wrongpass"}
    current = configured_app.post('/authentication/login', data=login_data,
                                  follow_redirects=True).data
    assert b'Invalid login' in current
