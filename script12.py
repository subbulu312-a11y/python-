class singletion:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
a =singletion()
b=singletion()
print(b is a)