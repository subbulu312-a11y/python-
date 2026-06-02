'''class Age:
    def __init__(self,value):
        if not isinstance(value,int)or value<0:
            raise ValueError(f'Invalid age:{value}')
        self.age=value
a =Age(25)
b=Age(-5)'''
class Student:
    school='python Academy'
    def __init__(self,name,age):
        self.name=name
        self.age=age
alice=Student('alice',21)
print(alice.__dict__)
print(Student.__dict__)