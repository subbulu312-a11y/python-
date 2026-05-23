l=[1,2,14,2,13]
def gen(x):
    match=-6
    for i in range(x):
        if i<match:
            match=i
        yield match
print(list(l))