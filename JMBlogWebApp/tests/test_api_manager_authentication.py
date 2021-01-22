import base64

def test_get_valid_code_for_valid_login(configured_app):
    credentials = base64.b64encode(b"admin:adminpass").decode('utf-8')
    login_token_code = (configured_app.post('/api/authentication/login',
                                            headers={"authorization": "Basic " + credentials})
                        .status_code)
    assert login_token_code == 200

def test_get_valid_code_for_invalid_login(configured_app):
    credentials = base64.b64encode(b"invalid:invalid").decode('utf-8')
    login_token_code = (configured_app.post('/api/authentication/login',
                                            headers={"authorization": "Basic " + credentials})
                        .status_code)
    assert login_token_code == 403

