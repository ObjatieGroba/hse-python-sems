def increaser(delta):
    def innercreaser(func):
        def inner(x):
            return func(x) + delta
        return inner
    return innercreaser


def timeit(func):
    def inner(*args, **kwargs):
        # start measure
        res = func(*args, **kwargs)
        # stop and print
        return res
    return inner

@increaser(4)
def func(x):
    return x

print(func(0))  # 4
