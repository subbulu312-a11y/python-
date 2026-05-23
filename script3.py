'''class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        if isinstance(o2,int):
            return self.x+o2
        if isinstance(o2,A):
            return self.x+o2.x
        else:
            print("Wrong class")
            return 0
a1=A(30)
a2=A(35)
print(a1+a2)'''
class c:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,o2):
        if isinstance(o2,str):
            return self.x+o2
        elif isinstance(o2,int):
            return self.y+o2
        else:
            return self.z+o2.z

c1=c("hello",2,3)
c2=c("bye",5,6)
print(c1+c2)
print(c1 + "hello")
print(c2+75)
