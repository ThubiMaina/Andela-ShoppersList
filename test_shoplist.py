import unittest
from shopperlist import ShopperList

class TestList(unittest.TestCase):
    """
    Perform unit testing for the shopperlist class
    """
    def setUp(self):
        """The setUp method before doing the tests"""
        self.newList = ShopperList()