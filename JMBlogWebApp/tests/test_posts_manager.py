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
    response = configured_app.get('/posts/?Page=2').data
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

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    response = configured_app.get('/posts/update/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                  follow_redirects=True).data

    assert b'Submit' in response

def test_logged_user_can_remove_own_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    response = configured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                  follow_redirects=True).data

    assert b'Remove' in response

def test_logged_user_cannot_edit_other_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/update/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                                   follow_redirects=True).status_code
    assert post_page == 403

def test_logged_user_cannot_remove_other_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/remove/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                                   follow_redirects=True).status_code
    assert post_page == 403

def test_logged_admin_can_edit_other_post(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                                   follow_redirects=True).data
    assert b'Edit' in post_page

def test_logged_admin_can_edit_other_post_other_author_first_author(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                   follow_redirects=True).data
    assert b'Edit' in post_page

def test_logged_admin_can_remove_post(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                                   follow_redirects=True).data
    assert b'Remove' in post_page

def test_logged_admin_can_edit_other_post_other_author(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                   follow_redirects=True).data
    assert b'Edit' in post_page

def test_logged_admin_can_remove_other_post_other_author(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                   follow_redirects=True).data
    assert b'Remove' in post_page

def test_logged_admin_can_edit_other_post_other_author_third(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/a656f973-5b82-462d-aff7-8d2c6c3e4fa2',
                                   follow_redirects=True).data
    assert b'Edit' in post_page

def test_logged_admin_can_remove_other_post_other_author_third(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/a656f973-5b82-462d-aff7-8d2c6c3e4fa2',
                                   follow_redirects=True).data
    assert b'Remove' in post_page

def test_pagination_for_added_post(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    added_post = {"NameInput":"TestTitle", "ContentInput":"TestContent"}

    configured_app.post('/posts/add', data=added_post, follow_redirects=True)

    post_page = configured_app.get('/posts/?Page=0', follow_redirects=True).data

    assert b'TestTitle' in post_page

def test_pagination_for_filter_applied(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    post_page = configured_app.get('/posts/?Users=FirstAuthor&Page=0', follow_redirects=True).data

    assert b'TestTitle' in post_page

def test_pagination_moves_post_to_next_page_if_number_exceeds(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    post_page = configured_app.get('/posts/?Page=2', follow_redirects=True).data

    assert b'FirstTitle' in post_page

def test_filtering_shows_no_posts_for_author_with_no_posts(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    post_page = configured_app.get('/posts/?Users=admin&Page=0', follow_redirects=True).data

    assert b'FirstTitle' or b'SecondTitle' or b'ThirdTitle' in post_page

def test_filtering_no_parameter_provided_in_url_provides_none_as_parameter_users(configured_app):

    post_page = configured_app.get('/posts/?Users=&Page=0', follow_redirects=True).data

    assert b'FirstTitle' or b'SecondTitle' or b'ThirdTitle' in post_page

def test_filtering_no_parameter_provided_in_url_provides_none_as_parameter_page(configured_app):

    post_page = configured_app.get('/posts/?Users=&Page=', follow_redirects=True).data

    assert b'FirstTitle' or b'SecondTitle' or b'ThirdTitle' in post_page

def test_pagination_gets_next_if_there_are_more_existing_posts(configured_app):

    post_page = configured_app.get('/posts', follow_redirects=True).data

    assert b'Next' in post_page and b'Previous' not in post_page

def test_pagination_gets_previous_if_there_are_no_more_posts_forward_only_backward(configured_app):

    post_page = configured_app.get('/posts/?Users=&Page=2', follow_redirects=True).data

    assert b'Previous' in post_page and b'Next' not in post_page

def test_pagination_gets_both_buttons_for_previous_and_next_pages(configured_app):
    login_data = {"NameInput": "admin", "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    post_page = configured_app.get('/posts/?Page=1', follow_redirects=True).data

    assert b'Previous' in post_page and b'Next' in post_page

def test_pagination_dissapears_if_no_further_posts_are_available(configured_app):

    post_page = configured_app.get('/posts/?Users=FirstAuthor', follow_redirects=True).data

    assert b'Next' not in post_page and b'Previous' not in post_page
