def test_setup_unconfigured_returns_load_page(current_app):
    response = current_app.get('/setup/').data
    assert b'Host' in response


def test_setup_returns_valid_response_for_sent_data(current_app):
    data = {
        'host': 'localhost',
        'user': 'postgres',
        'database' : 'testdb',
        'password': 'testpass'}
    post_response = current_app.post('/setup', data=data, follow_redirects=True).status_code
    assert post_response == 200