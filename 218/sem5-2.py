import time


def test_func():
    print(1)


class Func:
    def __call__(self, *args, **kwargs):
        return 1111111

f = Func()
print(f())


def decorator_generator(delta):
    def decorator(func):
        def inner(x):
            start = time.time()
            res = func(x + delta)
            end = time.time()
            return res, end - start
        return inner
    return decorator


@decorator_generator(5)
def same(x):
    time.sleep(0.5)
    return x

# same = decorator(same)

print(same(3))



