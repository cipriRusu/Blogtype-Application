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

def test_add_post_route_status_code(configured_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}
    post_response = configured_app.post('/posts/add', data=data).status_code
    assert post_response == 302

def test_add_post_route_check_content_after_post(configured_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}

    post_response = configured_app.post('/posts/add', data=data, follow_redirects=True).data

    assert b'NewName' in post_response

def test_add_post_route_check_content_in_listing_after(configured_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}

    add_post = configured_app.post('/posts/add', data=data, follow_redirects=True)
    assert add_post.status_code == 200

    after_add = configured_app.get('/', follow_redirects=True).data

    assert b'NewName' in after_add

def test_remove_post_route_check_content_in_listing_after(configured_app):
    remove_post = configured_app.get('/posts/remove/f9c3a576-28bc-4b63-931d-04d6488d2f0d'
                                     , follow_redirects=True).data
    assert b'FirstTitle' not in remove_post

def test_edit_post_route_check_content_in_post_after_edit(configured_app):

    data = {"NameInput": "NewName",
            "AuthorInput": "NewAuthor",
            "ContentInput": "NewContent"}

    edit_post = configured_app.post('/posts/update/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                                    data=data, follow_redirects=True).data

    assert b'SecondTitle' not in edit_post
    assert b'NewName' in edit_post

def test_setup_manager_redirect_if_valid_configuration(configured_app):
    returned_page = configured_app.get('/setup/', follow_redirects=True).data
    assert b"Blog App" in returned_page

def test_setup_manager_does_not_redirect_if_unconfigured(unconfigured_app):
    returned_page = unconfigured_app.get('/setup/', follow_redirects=True).data
    assert b"Connection Setup:" in returned_page
