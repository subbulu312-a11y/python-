from abc import ABC, abstractmethod
from email.mime import application


class BaseAbstract(ABC):
    @abstractmethod
    def abstract_method_one(self):
        pass
    @abstractmethod
    def abstract_method_two(self):
        pass
class DerivedAbstract(BaseAbstract):
    def __init__(self,application_name):
        self.application_name = application_name
        print(f"{self.application_name} derivedabstract constructor initialized.")
    def normal_defined_method(selfs):
        print(f"{selfs.application_name} excuting normal_defined_method from derivedabstract.")
    @abstractmethod
    def abstract_method_three(self):
        pass
    @abstractmethod
    def abstract_method_four(self):
        pass
class ConcreteClass(DerivedAbstract):
    def __init__(self,application_name):
        super().__init__(application_name)
    def abstract_method_one(self):
        print(f"{self.application_name} concrete implementation of abstract method one.")
    def abstract_method_two(self):
        print(f"{self.application_name} concrete implementation of abstract method two.")
    def abstract_method_three(self):
        print(f"{self.application_name} concrete implementation of abstract method three.")
    def abstract_method_four(self):
        print(f"{self.application_name} concrete implementation of abstract method four.")
if __name__=="__main__":
    application=ConcreteClass(application_name="OOP Demo App")
    print("\n--excuting methods---")
    application.abstract_method_one()
    application.abstract_method_two()
    application.abstract_method_three()
    application.abstract_method_four()