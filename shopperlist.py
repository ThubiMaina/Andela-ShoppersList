lists = {}
shoppingItems = []
"""an empty list to store my items"""
class ShopperList(object):
    ShopperLists = {}
    
    def __init__(self,name=None, description=None, owner = None ):
        """ Initializing  class instance variables"""
        self.name = name
        self.description = description
        self.owner = owner
    def create(self, name, description):
        """defining method to create shop list"""
        if description != ''and name != '':
            if lists != {}:
                if name not in lists.keys():
                    self.ShopperLists[name] = {
                    'description':description,
                    'name':name,
                    }
                    return 1
                else:
                    return 2
            else:
                self.ShopperLists[name] = {
                'description':description,
                'name':name,
                }
                return 1
        else:
            return 3 

    def createitem(self, name, item):
        """defining method to create an item in a shoppinglist"""
        if item != '':
            shoppingItems.append({'item': item, 'name': name})
            return 1
        return 2    

    def get_shoppinglist(self) :
        return self.ShopperLists

    def delete(self, name):
        """defining method to delete shopping  list"""
        if name in self.ShopperLists.keys():
            #checks if the name being deleted exists
            del self.ShopperLists[name]
            return True
        else:
            return 2 