'''class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f'{self.name} makes a sound'
class Dog(Animal):
    def fetch(self):
        return f'{self.name} fetch the ball!'
d=Dog('rex')
print(d.speak())
print(d.fetch())'''
class vechicle:
    def start(self): return 'vechicle started'
class car(vechicle):
    def drive(self): return 'car is driving'
class electriccar(car):
    def charge(self): return 'charging battery...'
d=electriccar()
print(d.start())
print(d.drive())
print(d.charge())
