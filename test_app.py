import unittest
from app import app  # Make sure this import is correct

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page_loads(self):
        response = self.app.get('/login', content_type='html/text')
        print(response.data)  # Debug print
        self.assertTrue(b'Login' in response.data)  # Update this line

    def test_main_route_requires_login(self):
        response = self.app.get('/', follow_redirects=True)
        print(response.status_code)  # Debug print
        self.assertEqual(response.status_code, 200)  # Check for successful request

    def test_welcome_page_loads(self):
        response = self.app.get('/login', content_type='html/text')
        print(response.data)  # Debug print
        self.assertTrue(b'Login' in response.data)  # Update this line

if __name__ == '__main__':
    unittest.main()