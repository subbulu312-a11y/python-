'''def power(base,exponent=2):
    return base^exponent
list=power(2,3)
print(list)
def connect(host,port=3306,protocol='tcp'):
    print(f"host={host},port={port} ,protocol={protocol}")
connect('localhost',3306,protocol='tcp')
def fun(*args):
    s=0
    for i in args:
        s=s+i
    return s
print(fun(10,20,30,40))
from codecs import namereplace_errors


def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")
fun(name="subbu",age=35)
def fun(a,b,*args,option='default',**kwargs):
    print(a,b,args,option,kwargs)
fun(1,2,3,4,5,complex=10,property=20)'''
def multiply(*args):
    if not args:
        return 1
    product=1
    for i in args:
        product=product*i
    return product
print(multiply(2,3,4))