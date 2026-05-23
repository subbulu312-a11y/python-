class B:
    def m1(self):
        print("b class")
@classmethod
def m2(cls):
    cls().m1()
    print("class method")
b1=B()
b1.m1()