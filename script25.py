from multiprocessing import resource_sharer

l=["hello",'hii',"who","are","you?"]
k=list(map(func,l))
def func(x):
    def func(y):
        if y not in "AEIOUaeiou":
            return y
        return ""
    re