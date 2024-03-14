
def my_factorial(n):
    if n == 0:
        yield 1
    else:
        previous = yield from my_factorial(n-1)
        yield n * previous
    
my_factorial(4)
