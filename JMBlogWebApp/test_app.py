import unittest
from app import app
from views import post_manager


class TestApp(unittest.TestCase):
    def test_app_response(self):
        post_manager.dataSource = 0
        tester = app.test_client(self)
        response = tester.get('/posts/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
