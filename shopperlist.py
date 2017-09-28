lists = {}

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
                if name not in my_list.keys():
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

    def get_shoppinglist(self) :
        return self.ShopperLists         
        