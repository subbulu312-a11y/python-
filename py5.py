from os import path
from threading import current_thread


def count_up(start,stop):
    current=start
    while current <= stop:
        yield current
        current=current+1
gen=count_up(1,5)
print(type(gen))
for n in gen:
    print(n,end=" ")