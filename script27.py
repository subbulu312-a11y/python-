import copy
class shopping_cart:
    def __init__(self):
        self.__items = []
    def add_item(self, item_name:str,price:float):
        """adds a new item to the cart."""
        item_name={"name":item_name,"price":price}
        self.__items.append(item_name)
        print(f"added:{item_name} (${price})")
    def remove_item(self,item_name:str):
        """ removes the first occurrence of an item by name"""
        for item in self.__items:
            if item["name"] == item_name:
                self.__items.remove(item)
                print(f"removed:{item_name}")
                return
        print(f"error:'{item_name}' not found in cart.")
    def get_items(self):
        """:return a safe copy of the cart items.
        modifying this retured list will not affect the internal cart state."""
        return copy.deepcopy(self.__items)
    def get_total_cost(self):
        """helper method to calculate total car cost"""
        return sum([item["price"] for item in self.__items])
if __name__=="__main__":
    my_cart=shopping_cart()
    print("--Adding Items---")
    my_cart.add_item("wireless mouse",1200.00)
    my_cart.add_item("mechanical keyboard",4500.00)
    print("\n__testing encapsulation__")
    try:
        print(my_cart.items)
    except AttributeError:
        print("success:cannot access 'my_cart.items' directly due to name mangling")
    extracted_items=my_cart.get_items()
    print("fetched items copy:",extracted_items)
    extracted_items.clear()
    print("modified external list:",extracted_items)
    print("actual cart total price after external attempt to clear:",my_cart.get_total_cost())
    print("\n--removing items--")
    my_cart.remove_item("wireless mouse")
    print("final safe copy of cart: ",my_cart.get_items())