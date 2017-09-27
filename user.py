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
        if re.match("[a-zA-Z0-9- .]+$",username):
            if username !='' and email !='' and password !='':
                if username not in users.keys():
                    if email not in users.keys():
                        if password ==cpassword:
                            regEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                            regPass = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$"
                            result = email
                            if re.search(regEmail ,result):
                                if re.search(regPass ,password):
                                    users[email] = {'email':email,
                                                    'username':username,
                                                    'password':password}
                                    return 1
                                return 7
                            return 2    
                        return 3
                    return 4
                return 5

            return 6
        
        return 8
    def login(self,username, password):
        """ defining method to Log in user"""
        if email != '' and password != '':
            if email in users.keys():
                result = users[email]
                password = result['pass']
                if password == password:
                    return 1
                return 2
            return 3
        return 4

