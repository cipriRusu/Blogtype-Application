def test_root_redirects(configured_app):
    response = configured_app.get('/').status_code
    assert response == 302

def test_root_unconfigured_redirects(unconfigured_app):
    response = unconfigured_app.get('/').status_code
    assert response == 302

def test_start_page_does_not_redirect_if_setup_present(configured_app):
    response = configured_app.get('/', follow_redirects=True).data
    assert b'Blog App' in response

def test_start_page_redirects_to_setup_if_setup_not_present(unconfigured_app):
    response = unconfigured_app.get('/', follow_redirects=True).data
    assert b'Connection Setup:' in response

def test_loading_contains_static_value(configured_app):
    response = configured_app.get('/posts/').data
    assert b'Blog App' in response

def test_browsing_to_posts_route_redirects_to_setup_automatically(unconfigured_app):
    response = unconfigured_app.get('/posts/', follow_redirects=True).data
    assert b'Connection Setup:' in response

def test_loading_contains_dynamic_value(configured_app):
    response = configured_app.get('/posts/').data
    assert b'FirstTitle' in response

def test_loading_returns_false_for_random_text(configured_app):
    response = configured_app.get('/posts/').data
    assert b'RandomText' not in response

def test_loading_cotains_static_value_post_page(configured_app):
    response = configured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d').data
    assert b'FirstTitle' in response

def test_post_page_redirects_to_setup_page(unconfigured_app):
    response = unconfigured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                    follow_redirects=True).data
    assert b'Connection Setup:' in response

def test_loading_contains_dynamic_value_post_page(configured_app):
    response = configured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d').data
    assert b'Specific content first post' in response

def test_logged_user_can_edit_own_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    logged_app = configured_app.post('/authentication/login', data=login_data, 
                                     follow_redirects=True)

    response = configured_app.get('/posts/update/f9c3a576-28bc-4b63-931d-04d6488d2f0d', 
                                  follow_redirects=True).status_code

    assert response == 200

def test_logged_user_can_remove_own_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}
    
    logged_app = configured_app.post('/authentication/login', data=login_data, 
                                     follow_redirects=True)

    response = configured_app.get('/posts/remove/f9c3a576-28bc-4b63-931d-04d6488d2f0d', 
                                  follow_redirects=True).status_code

    assert response == 200

def test_logged_user_cannot_edit_other_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}
    
    logged_app = configured_app.post('/authentication/login', data=login_data, 
                                     follow_redirects=True)

    post_page = configured_app.get('/posts/update/daca57d1-c180-4e0a-8394-f5c95a5d5f23', 
                                  follow_redirects=True).status_code
    assert post_page == 403

def test_logged_user_cannot_remove_other_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}
    
    logged_app = configured_app.post('/authentication/login', data=login_data, 
                                     follow_redirects=True)

    post_page = configured_app.get('/posts/remove/daca57d1-c180-4e0a-8394-f5c95a5d5f23', 
                                  follow_redirects=True).status_code
    assert post_page == 403
