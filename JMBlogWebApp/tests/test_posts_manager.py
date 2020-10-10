def test_root_redirects(current_app):
    response = current_app.get('/').status_code
    assert response == 302

def test_loading_contains_static_value(current_app):
    response = current_app.get('/posts/').data
    assert b'Blog App' in response

def test_loading_contains_dynamic_value(current_app):
    response = current_app.get('/posts/').data
    assert b'FirstTitle' in response

def test_loading_returns_false_for_random_text(current_app):
    response = current_app.get('/posts/').data
    assert b'RandomText' not in response

def test_loading_cotains_static_value_post_page(current_app):
    response = current_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d').data
    assert b'FirstTitle' in response

def test_loading_contains_dynamic_value_post_page(current_app):
    response = current_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d').data
    assert b'Specific content first post' in response

def test_add_post_route_status_code(current_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}
    post_response = current_app.post('/posts/add', data=data).status_code
    assert post_response == 302

def test_add_post_route_check_content_after_post(current_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}

    post_response = current_app.post('/posts/add', data=data, follow_redirects=True).data

    assert b'NewName' in post_response

def test_add_post_route_check_content_in_listing_after(current_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}

    add_post = current_app.post('/posts/add', data=data, follow_redirects=True)
    assert add_post.status_code == 200

    after_add = current_app.get('/', follow_redirects=True).data

    assert b'NewName' in after_add

def test_remove_post_route_check_content_in_listing_after(current_app):
    remove_post = current_app.get('/posts/remove/f9c3a576-28bc-4b63-931d-04d6488d2f0d'
                                  , follow_redirects=True).data
    assert b'FirstTitle' not in remove_post

def test_edit_post_route_check_content_in_post_after_edit(current_app):
    data = {
        'NameInput': 'NewName',
        'AuthorInput': 'NewAuthor',
        'ContentInput': 'NewContent'}

    edit_post = current_app.post('/posts/update/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                                 data=data, follow_redirects=True)

    assert b'SecondTitle' not in edit_post.data
    assert b'NewName' in edit_post.data
