'''class flyable:
    def fly(self): return 'i can fly!'
class swimmable:
    def swim(self): return 'i can swim!'
class Duck(flyable,swimmable):
    def quack(self): return 'quack!'
d=Duck()
print(d.fly())
print(d.swim())
print(d.quack())'''
from logging import setLogRecordFactory


class shape:
    def area(self): return 0
class circle(shape):
    def __init__(self,r): self.r=r
    def area(self): return 3.14*self.r**2
class rectangle(shape):
    def __init__(self,w,h) : self.w,self.=w,h
    def area(self): return self.w*self.h
print(circle(5).area())
print(rectangle(4,6).area())