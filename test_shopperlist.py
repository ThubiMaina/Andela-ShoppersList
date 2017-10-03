import unittest
from shopperlist import ShopperList

class TestList(unittest.TestCase):
    """
    Perform unit testing for the shopperlist class
    """
    def setUp(self):
        """The setUp method before doing the tests"""
        self.lists = ShopperList()       
        self.lists.ShopperLists = {}

    def test_for_creating_a_shopperlist(self):
        """ defining method to test for Creating a shoppers list """
        self.lists.ShopperLists = {}
        current_count = len(self.lists.ShopperLists)
        output = self.lists.create('Grocery', 'Fresh farm produce')
        self.assertEqual(current_count+1, output, "List successfully created")

    def test_if_name_empty(self):
        """defining method to test for adding a shopping list with an empty name """
        output = self.lists.create('',  'fresh')
        self.assertEqual(3, output, "please fill all fields")

    def test_if_description_empty(self):
        """defining method to test for adding a shopper list with an empty description"""
        output = self.lists.create('Grocery', '' )
        self.assertEqual(3, output, "please fill the description") 

    def tests_if_list_exists(self):
        """defining method to test for adding a shop list That already exists """
        self.lists.create('Grocery','Fresh Produce')
        output = self.lists.create('Grocery','Fresh Produce')
        self.assertEqual(1, output, "That list already exists!")

    def tests_delete_list(self):
        """defining method to test for deleting a shopperlist"""
        self.lists.ShopperLists = {}
        self.lists.create('Grocery','Fresh Produce')
        output = self.lists.delete('Grocery')
        self.assertEqual(1, output, "Succesfully deleted!")

    def tests_delete_list_that_does_not_exist(self):
        """defining method to test for deleting a shoppinglist That doesnot exist""" 
        self.lists.ShopperLists = {}
        self.lists.create('Grocery','Fresh Produce')
        output = self.lists.delete('Household')
        self.assertEqual(2, output, "You can not delete a list that does not exist")

    def tests_Add_item(self):
        """defining method to test adding an item in a Shoppinglist"""
        self.lists.ShopItems = []
        current_count = len(self.lists.ShopItems)
        output = self.lists.createitem('mango')
        self.assertEqual(current_count+1, output, "Item successfully added")

    def tests_addEmpty_item(self):
        """defining method to test adding an empty item in a shoppinglist"""
        self.lists.ShopItems = []
        output = self.lists.createitem('')
        self.assertEqual(2,output,"Cannot add an empty item ")                  
           

if __name__ =='main':
    unittest.main()    
    