# test_app.py
import unittest
from ..app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_home_route(self):
        # Test the home route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Simple Web App", response.data)
    
    def test_template_rendering(self):
        # Test if the index template is rendered correctly
        response = self.app.get('/')
        self.assertIn(b"Simple Web App", response.data)
        self.assertIn(b"alt=\"guitar player at concert\"", response.data)

    def test_nonexistent_route(self):
        # Test a route that doesn't exist
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()