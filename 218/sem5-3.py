def some_func(x, y, z=5):
    print(x + y + z)

def f(extra, *args, **kwargs):
    print(args)
    print(kwargs)
    kwargs.pop('z')
    some_func(*args, **kwargs)


f(1, 2, 3, z=4)
