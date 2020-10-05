import unittest
from app import app
from views import post_manager


class TestApp(unittest.TestCase):
    def test_app_response(self):
        tester = app.test_client(self)
        response = tester.get('/posts/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_app_main_header(self):
        tester = app.test_client(self)
        response = tester.get('/posts/', content_type='html/text')
        self.assertTrue(b'Blog App' in response.data)

    def test_app_dynamic_content(self):
        post_manager.dataSource = 0
        tester = app.test_client(self)
        response = tester.get('/posts/', content_type='html/text')
        self.assertTrue(b'FirstTitle' in response.data)

if __name__ == '__main__':
    unittest.main()
