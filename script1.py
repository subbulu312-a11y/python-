class variable():
    def __init__(self,name,category,price,quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        if quantity>10:
            return quantity
        else:
            return 0
    def __init__(cls,product_str):


