class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f'{self.name} makes a sound'
class Dog(Animal):
    def fetch(self):
        return f'{self.name} fetch the ball!'
d=Dog('rex')
print(d.speak())
print(d.fetch())
