'''def squares_list(n):
    result=[]
    for i in range(n):
        result.append(i*i)
    return result
print(squares_list(5))'''
'''def squares_gen(n):
    for i in range(n):
        yield i*i
gen=squares_gen(5)
print(list(gen))'''
def demo():
    print("step 1")
    yield 'A'
    print("step 2")
    yield 'B'
    print("step 3")
    yield 'C'
    print("step 4")
    yield StopIteration
g=demo()
print(next(g))
print(next(g))
print(next(g))
print(next(g))