
import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Perform unit testing for the User class
    """
    def setUp(self):
        """The setUp method before doing the tests"""
        self.newUser = User()

    def test_create_account(self):
        """ method to test for creating user account"""
        self.newUser.users = {}
        current_count = len(self.newUser.users)
        result = self.newUser.register( 'email@mail.com', 'name', '1234', '1234')
        self.assertEqual(1, result, "User succesfully created")

    def test_null_username(self):
        """method to checking when user name is empty"""
        result = self.newUser.register('erick@gmail.com','','1234','1234')
        self.assertEqual(6 ,result,'User name cannot be empty')
    
    def test_null_email(self):
        """method to check if the email is empty"""
        result = self.newUser.register('','Erick','1234','1234')
        self.assertEqual(6,result,'Email cannot be empty')

    def test_null_password(self):
        """"""
        result = self.newUser.register('erick@gmail.com','Erick','', '1234')
        self.assertEqual(6,result,'enter the password')

    def test_password_and_cpassword_match(self):
        result = self.newUser.register('erick@gmail.com','Erick', '1234','124')
        self.assertEqual(3,result,'passwords do not match')

    def test_email_exists(self):
        self.newUser.users = {} 
        self.newUser.register('erick@gmail.com','Erick','1234','1234')
        result = self.newUser.register('erick@gmail.com','Erick','1234','1234')
        self.assertEqual(4,result,'This email has been registered')
if __name__ =='main':
    unittest.main()