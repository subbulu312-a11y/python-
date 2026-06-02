class Animal:
class Dog(Animal):
class Cat(Animal):
rex = Dog()
print(isinstance(rex, Dog))
print(isinstance(rex, Animal))
print(isinstance(rex, Cat))
print(isinstance(rex, object))