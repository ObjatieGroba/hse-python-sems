x = 10

def xcreaser(x):
    def inner_func(y):
        nonlocal x
        res = x + y
        x = y + 1
        return res
    def inner2_func():
        return x
    return inner_func, inner2_func

two_creaser, extra = xcreaser(2)
print(two_creaser(3))
print(x)
print(two_creaser(0))
print(extra())

