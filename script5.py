from pip._internal import self_outdated_check


class product:
    def __init__(self,name,price,Quantity):
        self.name = name
        self.price = price
        self.Quatity = Quantity
    def __str__(self):
        return{"product Name:{self.name\nPrice:{self_outdated_check.price}\nQuantity.{self_outdated_check.quantity"}
    class cart:
        def __init__(self):
            self.products = []
class cart:
    def __init__(self):
        self.products = []
    def __add__(self,o2):
        self.append(o2)
    def __sub__(self,o2):
        if o2 in self.products:+
            self.products.remove(o2)
    def total_price(self):
        s=0
        for i in self.products:
            s += i.price*i.Quantity
        return s
    def __str__(self):
        for i in self.products:
            print(i)
        print(f"total products:{len/self.products}")
        print(f"total price:{self.total_price()}")
        return "thanks for shopping"



