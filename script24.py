


class rectangle:
    def __init__(self,l,b):
        self.l= l
        self.b= b
class square:
    def __init__(self,a):
        self.a = a
class circle:
    def __init__(self,r):
        self.r = r
class triangle:
    def __init__(self,b,h):
        self.b = b
        self.h = h
class shape:
    def area(self,v):
        if isinstance(v,rectangle):
            print(f"area of rectangle:{v.l*v.b}")
        elif isinstance(v,square):
            print(f"area of square:{v.a**2}")
        elif isinstance(v,circle):
            print(f"area of circle:{3.14*v.r**2}")
        elif isinstance(v,triangle):
            print(f"area of triangle:{1/2*v.b*v.h}")
        else:
            print()
r1=rectangle(10,20)
s1=square(2)
c1=circle(2)
t1=triangle(5,5)
v=shape()
v.area(r1)
v.area(s1)
v.area(c1)
v.area(t1)
