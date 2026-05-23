from script7 import b1


class A:
    def m1(self):   
        print("A")
        super().m1()
class B:
    def m1(self):
        print("B")
        super().m1()
class C:
    def m1(self):
        print("C")
class D:
    def m1(self):
        print("D")
        super().m1()
a1=A()
a1.m1()
b1=B()
b1.m1()
c1=C()
c1.m1()
d1=D()
d1.m1()
print(D)