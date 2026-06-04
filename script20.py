class temperatur:
    def __init__(self,celsius):
        self.__celsius=celsius
    @property
    def celsius(self):
        return self.__celsius
    @property
    def fahrenheits(self):
        return self.__celsius*9/5+32
t=temperatur(1000)
print(t.celsius)
print(t.fahrenheits)
t.celsius