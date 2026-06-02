from itertools import count
from logging import setLogRecordFactory

class Countup:
    def __init__(self,start,stop):
        self.current= start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value=self.current
        self.current+=1
        return value
counter=Countup(1,5)
for n in counter:
    print(n,end=' ')