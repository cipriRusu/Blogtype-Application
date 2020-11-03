def test_setup_manager_redirect_if_valid_configuration(configured_app):
    returned_page = configured_app.get('/setup/', follow_redirects=True).data
    assert b"Blog App" in returned_page

def test_setup_manager_does_not_redirect_if_unconfigured(unconfigured_app):
    returned_page = unconfigured_app.get('/setup/', follow_redirects=True).data
    assert b"Connection Setup:" in returned_page
