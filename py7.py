'''def squares_list(n):
    result=[]
    for i in range(n):
        result.append(i*i)
    return result
print(squares_list(5))'''
def squares_gen(n):
    for i in range(n):
        yield i*i
gen=squares_gen(5)
print(list(gen))