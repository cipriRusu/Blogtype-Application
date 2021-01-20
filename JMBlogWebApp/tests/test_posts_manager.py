import io
import base64
from repository.in_memory_data import in_memory_photos

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
    response = configured_app.get('/posts/?Page=1').data
    assert b'FirstTitle' in response

def test_loading_returns_false_for_random_text(configured_app):
    response = configured_app.get('/posts/').data
    assert b'RandomText' not in response

def test_loading_cotains_static_value_post_page(configured_app):
    response = configured_app.get('/api/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d').data
    assert b'FirstTitle' in response

def test_post_page_redirects_to_setup_page(unconfigured_app):
    response = unconfigured_app.get('/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d',
                                    follow_redirects=True).data
    assert b'Connection Setup:' in response

def test_loading_contains_dynamic_value_post_page(configured_app):
    response = configured_app.get('/api/posts/f9c3a576-28bc-4b63-931d-04d6488d2f0d').data
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

    added_post = {"NameInput":"TestTitle",
                  "ContentInput":"TestContent",
                  'Image-File': (io.BytesIO(b'test_image_content'), "test.jpg")}

    configured_app.post('/posts/add',
                        content_type='multipart/form-data',
                        data=added_post,
                        follow_redirects=True)

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

def test_post_addition_adds_no_image_if_none_is_selected(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login',
                        data=login_data,
                        follow_redirects=True)

    added_post = {"NameInput":"TestTitle",
                  "ContentInput":"TestContent",
                  'Image-File':(io.BytesIO(b''), '')}

    response_data = configured_app.post('/posts/add',
                                        content_type='multipart/form-data',
                                        data=added_post,
                                        follow_redirects=True).data

    assert in_memory_photos['default'].encode() in response_data

def test_post_loads_image_if_image_exists(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    response_data = configured_app.get('/api/posts/a656f973-5b82-462d-aff7-8d2c6c3e4fa2',
                                       follow_redirects=True).data

    assert in_memory_photos['local3'].encode('utf-8') in response_data

def test_post_loads_default_image_if_image_is_removed(configured_app):
    login_data = {"NameInput": "SecondAuthor", "PasswordInput": "spass"}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    print(configured_app.post('/posts/update/daca57d1-c180-4e0a-8394-f5c95a5d5f23',
                              data={'Remove-Image': '',
                                    'NameInput': 'Test',
                                    'ContentInput': 'Test',
                                    'Image-File': (io.BytesIO(b''), "")},
                              follow_redirects=True).data)

    after_edit = configured_app.get('/api/posts/daca57d1-c180-4e0a-8394-f5c95a5d5f23').data

    assert in_memory_photos['default'].encode('utf-8') in after_edit

def test_post_changes_image_when_new_image_is_loaded(configured_app):
    login_data = {"NameInput": "ThirdAuthor", "PasswordInput": "tpass"}

    post_data = {'NameInput': 'Test',
                 'ContentInput': 'Test',
                 'Image-File': (io.BytesIO(b'test_image_content'), "test.jpg")}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    configured_app.post('/posts/update/2bb62474-43fb-4643-b38e-a333f3999254',
                        data=post_data,
                        follow_redirects=True).data

    encoded_image_data = base64.b64encode(b'test_image_content')

    response_json_data = configured_app.get('/api/posts/2bb62474-43fb-4643-b38e-a333f3999254').data

    assert encoded_image_data in response_json_data

def test_post_default_image_is_replaced_if_new_image_is_loaded(configured_app):
    login_data = {"NameInput": "FirstAuthor", "PasswordInput": "fpass"}

    post_data = {'NameInput': 'Test',
                 'ContentInput': 'Test',
                 'Image-File': (io.BytesIO(b'test_image_content'), "test.jpg")}

    configured_app.post('/authentication/login', data=login_data, follow_redirects=True)

    configured_app.post('/posts/update/3cb862a3-3bf7-44a2-83d8-7b7440588b68',
                        data=post_data,
                        follow_redirects=True).data

    encoded_image_data = base64.b64encode(b'test_image_content')

    returned_json_after_edit = (configured_app
                                .get('/api/posts/3cb862a3-3bf7-44a2-83d8-7b7440588b68')
                                .data)
    assert encoded_image_data in returned_json_after_edit

def test_post_flash_message_for_no_selected_image(configured_app):
    login_data = {"NameInput": "admin",
                  "PasswordInput": "adminpass"}

    post_data = {'Update-Picture': '',
                 'NameInput': 'Test',
                 'ContentInput': 'Test',
                 'Image-File': (io.BytesIO(b''), "")}

    configured_app.post('/authentication/login',
                        data=login_data,
                        follow_redirects=True)

    response_data = configured_app.post('/posts/update/0d816f70-0ed1-4cee-b156-112462e6ea52',
                                        data=post_data,
                                        follow_redirects=True).data

    assert b'No image uploaded' in response_data

def test_post_flash_message_for_illegal_format_selected_as_image(configured_app):
    login_data = {"NameInput": "admin",
                  "PasswordInput": "adminpass"}

    post_data = {'Update-Picture': '',
                 'NameInput': 'TestName',
                 'ContentInput': 'TestContent',
                 'Image-File': (io.BytesIO(b'test_illegal_content'), 'illegal.exe')}

    configured_app.post('/authentication/login',
                        data=login_data,
                        follow_redirects=True)

    response_data = configured_app.post('/posts/update/0d816f70-0ed1-4cee-b156-112462e6ea52',
                                        data=post_data,
                                        follow_redirects=True).data

    assert b'Invalid file type! Make sure a valid file format is selected' in response_data

def test_post_flash_message_for_default_image_to_remove(configured_app):
    login_data = {"NameInput": "admin",
                  "PasswordInput": "adminpass"}

    post_data = {'Remove-Picture':'',
                 'NameInput': 'TestName',
                 'ContentInput': 'TestContent',
                 'Image-File': (io.BytesIO(b''), '')}

    configured_app.post('/authentication/login',
                        data=login_data,
                        follow_redirects=True)

    response_data = configured_app.post('/posts/update/0d816f70-0ed1-4cee-b156-112462e6ea52',
                                        data=post_data,
                                        follow_redirects=True).data

    assert b'No photo found, nothing to remove' in response_data
