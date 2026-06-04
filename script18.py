from random import paretovariate


class person:
    def __init__(self,first_name:str,last_name:str):
        self.first_name=first_name
        self.last_name=last_name
    @property
    def first_name(self)-> str:
        return self._first_name
    @first_name.setter
    def first_name(self,value:str):
        self._first_name=value.strip()
    @property
    def last_name(self)-> str:
        return self._last_name
    @last_name.setter
    def last_name(self,value:str):
        self._last_name=value.strip()
    @property
    def full_name(self)-> str:
        return f"{self.first_name} {self.last_name}"
    @full_name.setter
    def full_name(self,full_name:str):
        parts=name_string.strip().split(" ",1)
        if len(parts)==2:
            self.first_name=parts[0]
            self.last_name=parts[1]
        else:
            self.first_name=parts[0]
            self.last_name=""
if __name__== "__main__" :
    person=person("subbu","hema")
    print(f"initial:{person.full_name}")
    person.full_name="subbulu"
    print(f"update first:{person.first_name}")
    print(f"update last:{person.last_name}")
    print(f"update full_name:{person.full_name}")
    person.first_name="subbu"
    print(f"after first name change:{person.first_name}")
