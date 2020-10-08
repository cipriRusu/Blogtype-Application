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
