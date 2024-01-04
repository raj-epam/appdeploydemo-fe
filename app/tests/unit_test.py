
import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_route(self):
        # Use the test client to make a request to the home route
        response = self.app.get('/fe')
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data contains a specific content
        self.assertIn(b"Welcome to Simple Web App", response.data)
    
    def test_template_rendering(self):
        # Test if the index template is rendered correctly
        response = self.app.get('/fe')
        self.assertIn(b"Simple Web App", response.data)
        self.assertIn(b"alt=\"guitar player at concert\"", response.data)

    def test_nonexistent_route(self):
        # Test a route that doesn't exist
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()