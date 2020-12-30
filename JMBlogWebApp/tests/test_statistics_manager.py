def test_returned_correct_statistics_at_start(configured_app):
    result_data = configured_app.get('/user_statistics', follow_redirects=True).data
    assert (b'2010' and b'April' and b'2 Posts' and
            b'May' and b'2 Posts' and b'2000' and
            b'April' and b'2 Posts' and b'June' and
            b'1 Posts' and b'July' and b'1 Posts' and
            b'1997' and b'February' and b'1 Posts' and
            b'March' and b'1 Posts' and b'April' and
            b'1 Posts' in result_data)

def test_returned_correct_statistics_at_start_for_selected_user(configured_app):
    result_data = configured_app.get('/user_statistics/?Users=ThirdAuthor',
                                     follow_redirects=True).data
    assert (b'2010' and b'May' and
            b'2 Posts' and b'2000' and
            b'July' and b'1 Posts' and
            b'1997' and b'April' and
            b'1 Posts' in result_data)

def test_returned_correct_statistics_after_removing_a_post(configured_app):
    login_data = {"NameInput": "ThirdAuthor",
                  "PasswordInput": "tpass"}

    configured_app.post('/authentication/login', data=login_data,
                        follow_redirects=True)

    print(configured_app.get('posts/remove/2bb62474-43fb-4643-b38e-a333f3999254',
                             follow_redirects=True).data)

    result_data = configured_app.get('/user_statistics/?Users=ThirdAuthor',
                                     follow_redirects=True).data

    assert b'July' not in result_data

def test_returned_the_same_if_post_is_edited(configured_app):
    login_data = {"NameInput": "admin",
                  "PasswordInput": "adminpass"}

    configured_app.post('/authentication/login',
                        data=login_data,
                        follow_redirects=True)

    post_data = {"update-post": "",
                 "NameInput": "TestTitle",
                 "ContentInput": "TestContent"}

    print(configured_app.post('/posts/update/2bb62474-43fb-4643-b38e-a333f3999254',
                              data=post_data,
                              follow_redirects=True).data)

    current_stats = configured_app.get('/user_statistics', follow_redirects=True).data

    assert (b'2010' and b'April' and b'2 Posts' and
            b'May' and b'2 Posts' and b'2000' and
            b'April' and b'2 Posts' and b'June' and
            b'1 Posts' and b'July' and b'1 Posts' and
            b'1997' and b'February' and b'1 Posts' and
            b'March' and b'1 Posts' and b'April' and
            b'1 Posts' in current_stats)

def test_returns_no_data_if_user_with_no_posts_is_selected(configured_app):
    result_data = configured_app.get('/user_statistics/?Users=admin',
                                     follow_redirects=True).data

    assert b'1997' and b'2000' and b'2010' not in result_data
