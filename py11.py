'''class A:
    def __init__(self,a):
        self.a=a
        class B(A):
            def __init__(self,a,b):
                super().__init__(a)
                self.b=b'''
class A:
    def m1(self):
        print('A class')
        class B(A):
            def m2(self):
                print('B class')
        class C(B):
            def m3(self):
                print('C class')
        class D(B):
            def m4(self):
                print('D class')
                super().m4()
                obj=D()
                print(D.mro())
                obj.m2()