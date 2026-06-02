'''def seasons():
    yield 'Spring'
    yield 'Summer'
    yield 'Autumn'
    yield 'Winter'
for s in seasons():
    print(s)'''
from tokenize import generate_tokens


def natural_numbers():
    n=1
    while True:
        yield n
        n +=1
gen=natural_numbers()
print([next(gen) for _ in range(6)])
