


users = {}

class User(object):
    """
    Class to handle  user functions
    """

    def __init__(self,username=None,location=None, email=None, password=None, cpassword=None ):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password
        self.location = location
        self.cpassword = cpassword

    def register(self, email, username,location, password, cpassword):
        pass
    
    def login(self,username, password):
        pass
