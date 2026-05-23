def my_decorator(fun):
    def wrapper(*args,**kwargs):
        result=fun(*args,**kwargs)
        if result<0:
            return 0
        return result
    return wrapper
@my_decorator
def sub(a,b):
    return a-b
final_output=sub(20,25)
print(final_output)