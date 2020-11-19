def test_redirects_user_manager(unconfigured_app):
    response = unconfigured_app.get('/users/').status_code
    assert response == 302

def test_forbidden_users_access_for_unlogged(configured_app):
    user_route_result = configured_app.get('/users',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_forbidden_user_data_access_for_unlogged(configured_app):
    user_route_result = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_forbidden_users_acceess_for_not_admin(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_forbidden_user_remove_route_access_for_logged_user_not_admin(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users/remove/6ee39856-2721-46c4-bda7-3faf8e4a60f5',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_allowed_user_edit_personal_data_for_own_profile(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users/update/6ee39856-2721-46c4-bda7-3faf8e4a60f5',
                                           follow_redirects=True).data
    assert b'Submit' in user_route_result

def test_forbidden_user_edit_personal_data_for_other_profile(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users/update/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_allow_acces_to_users_listing_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users',
                                           follow_redirects=True).data

    assert b'FirstAuthor' in user_route_result

def test_allow_access_to_user_data_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).data

    assert b'Username: ' in user_route_result
    assert b'SecondAuthor' in user_route_result

def test_allow_acces_to_user_edit_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).data

    assert b'Edit' in user_route_result

def test_allow_acces_to_user_remove_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    user_route_result = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).data

    assert b'Remove' in user_route_result
