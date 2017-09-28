import re


users = {}

class User(object):
    """
    Class to handle  user functions
    """

    def __init__(self,username=None, email=None, password=None, cpassword=None ):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password
        self.cpassword = cpassword

    def register(self, email, username, password, cpassword):
        if username != '' and email != '' and password !='':
            if re.match("[a-zA-Z0-9- .]+$", username):
                    if email not in users.keys():
                        if password == cpassword:
                            regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                            result = email
                            if re.search(regex ,result):
                                    users[email] = {'email':email,
                                                    'username':username,
                                                    'password':password
                                                    }
                                    return 1
                            return 2    
                        return 3
                    return 4
            return 8
        return 6

    def login(self,email, password):
        """ defining method to Log in user"""
        if email != '' and password != '':
            if email in users.keys():
                result = users[email]
                password = result['password']
                if password == password:
                    return 1
                return 2
            return 3
        return 4

    def get_user_name(self, email):
        if email in users.keys():
            result = users[email]
            return result['username']
        return False

    def get_user_email(self, email):
        if email in users.keys():
            result = users[email]
            return result['email']
        return False
