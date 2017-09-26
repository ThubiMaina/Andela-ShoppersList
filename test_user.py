import sys
import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Perform unit testing for the User class
    """
def setUp(self):
    """"""
    self.newUser = User()

def test_create_account(self):
    """defining method to test for creating user account"""
    # self.newUser.users = {}
    # current_count = len(self.newUser.users)
    # result = self.newUser.register( 'email@mail.com', 'name','Thika', 'erick', 'erick')
    # self.assertEqual(current_count+1, result, "User succesfully created")

def test_null_username(self):
    output = self.newUser.register('erick@gmail.com','','Thika','1234','1234')
    self.assertEqual(value ,output,'Username cannot be empty')


if __name__ =='main':
    unittest.main()