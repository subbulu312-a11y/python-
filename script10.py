from script7 import b1


class A:
    @classmethod
    def m1(cls):
        print("m1")
class B:
    @classmethod
    def m2(cls):
        super().m1()
        print("B class")
b1=B()
