import time

def deco_func(orig_func):
    def wrapper_func(*args, **kwargs):
        t1 = time.time_ns()
        result = orig_func(*args, **kwargs)
        t2 = time.time_ns() - t1
        print(t2)
        return result
    return wrapper_func

@deco_func
def display(a,b):
    print(f'values are {a} and {b}')

display(4,5)