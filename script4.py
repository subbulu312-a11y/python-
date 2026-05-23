from script7 import b1


class A:
    x=0
    def m1(self):
        print("A class")
class B(A):
    pass
b1=B()
class C:
    def m1(self):
        a1=A()
        a1.m1()
        print("c class")
c1=C()
c1.m1()