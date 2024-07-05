import unittest, sys

sys.path.append('../flask-hosting-template') # imports python file from parent directory
from app import app, db, User #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_home_page(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def register(self, username, email, password):
            return self.app.post('/register', data=dict(
                username=username,
                email=email,
                password=password,
                confirm_password=password
            ), follow_redirects=True)

    def test_register_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_invalid_username_registration(self):
        response = self.register('t', 'test@example.com', 'FlaskIsAwesome')
        self.assertIn(b'Field must be between 2 and 20 characters long.',
                      response.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email_registration(self):
        response = self.register('test2', 'test@example', 'FlaskIsAwesome')
        self.assertIn(b'Invalid email address.', response.data)
        self.assertEqual(response.status_code, 200)

    # def test_webhook_post_success(self):
    #     response = self.app.get('/update_server', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Updated PythonAnywhere successfully',
                        # response.data)

    # def test_webhook_post_failure(self):
    #   response = self.app.get('/update_server', follow_redirects=True)
    #   self.assertEqual(response.status_code, 400)
    #   self.assertIn(b'Wrong event type', response.data)
        

if __name__ == "__main__":
    unittest.main()