


class Demo:
    def __new__(cls):
        print("1. __new__called-allocating memory")
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        print("2. __init-- called-initiallising the object")
d=Demo()
