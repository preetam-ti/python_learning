#recursion way:
def feb(n):
    if n<=1:
        return n
    else:
        return feb(n-1)+feb(n-2)
n=5
for i in range(n):
    out = feb(i)
    print(out)

#using generator:
a = 10

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))

##simple fib program for series:
a = 10

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

print(fib(a))