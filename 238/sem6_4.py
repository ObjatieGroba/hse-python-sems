def cached(func):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return inner

@cached
def fib(x):
    print(1)
    if x == 0 or x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)
