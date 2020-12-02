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

    print(configured_app.post('/authentication/login', data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_forbidden_user_remove_route_access_for_logged_user_not_admin(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    print(configured_app.post('/authentication/login', data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users/remove/6ee39856-2721-46c4-bda7-3faf8e4a60f5',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_allowed_user_edit_personal_data_for_own_profile(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    print(configured_app.post('/authentication/login', data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users/update/6ee39856-2721-46c4-bda7-3faf8e4a60f5',
                                           follow_redirects=True).data
    assert b'Submit' in user_route_result

def test_forbidden_user_edit_personal_data_for_other_profile(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    print(configured_app.post('/authentication/login', data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users/update/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).status_code
    assert user_route_result == 403

def test_allow_acces_to_users_listing_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    print(configured_app.post('/authentication/login', data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users',
                                           follow_redirects=True).data

    assert b'FirstAuthor' in user_route_result

def test_allow_access_to_user_data_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    print(configured_app.post('/authentication/login', data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).data

    assert b'Username: ' in user_route_result
    assert b'SecondAuthor' in user_route_result

def test_allow_acces_to_user_edit_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    print(configured_app.post('/authentication/login',
                              data=login_data,
                              follow_redirects=True))

    user_route_result = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                           follow_redirects=True).data

    assert b'Edit' in user_route_result

def test_allow_acces_to_user_remove_for_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    print(configured_app.post('/authentication/login',
                              data=login_data,
                              follow_redirects=True))

    after_removal_data = configured_app.get('/users/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                                            follow_redirects=True).data
    assert b'Remove' in after_removal_data

def test_removing_user_removes_post_also(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    print(configured_app.post('/authentication/login',
                              data=login_data, follow_redirects=True))

    print(configured_app.get('/users/remove/25447284-aa74-4fb6-b7a0-2bb955f2b2b1',
                             follow_redirects=True))

    posts_page = configured_app.get('/posts', follow_redirects=True).data

    assert b'SecondAuthor' not in posts_page

def test_edit_user_edits_posts_names_also_by_admin(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    print(configured_app.post('/authentication/login',
                              data=login_data,
                              follow_redirects=True))

    edit_data = {"UserNameInput": "FirstEditedInput",
                 "UserEmailInput": "editemail@gmail.com",
                 "UserPassInput": "test"}

    print(configured_app.post('/users/update/99ae0e65-372b-4f4a-be88-776d6a4d92bd',
                              data=edit_data,
                              follow_redirects=True).status_code)

    edited_posts = configured_app.get('/posts', follow_redirects=True).data

    assert b'FirstEditedInput' in edited_posts

def test_edit_user_edits_posts_names_also_by_user(configured_app):
    login_data = {"NameInput": "FirstEditedInput", "PasswordInput": "test"}

    print(configured_app.post('/authentication/login',
                              data=login_data,
                              follow_redirects=True))

    edit_data = {"UserNameInput": "SecondEditedInput",
                 "UserEmailInput": "editemail@gmail.com",
                 "UserPassInput": "test"}

    print(configured_app.post('/users/update/99ae0e65-372b-4f4a-be88-776d6a4d92bd',
                              data=edit_data,
                              follow_redirects=True))

    edited_posts = configured_app.get('/posts', follow_redirects=True).data

    assert b'SecondEditedInput' in edited_posts

def test_add_user_allows_with_user_that_exists(configured_app):
    login_data = {"NameInput": "ThirdAuthor", "PasswordInput": "tpass"}

    print(configured_app.post('/authentication/login',
                              data=login_data,
                              follow_redirects=True))

    add_data = {"NameInput": "UpdatedTitleByUser", "ContentInput":"TestContentAdded"}

    print(configured_app.post('/posts/add',
                              data=add_data,
                              follow_redirects=True))

    all_posts = configured_app.get('/posts', follow_redirects=True).data

    assert b"UpdatedTitleByUser" in all_posts

def test_add_user_not_allowing_if_no_user_logged_in(configured_app):
    add_data = {"NameInput": "IllegalAdd", "ContentInput":"IllegalAdd"}

    print(configured_app.post('/posts/add',
                              data=add_data,
                              follow_redirects=True))

    all_posts = configured_app.get('/posts', follow_redirects=True).data

    assert b'IllegalAdd' not in all_posts
