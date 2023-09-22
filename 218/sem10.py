import time
import typing as tp


def some_func(x):
    return x + 1


# def static_applier(func: tp.Callable) -> tp.Callable:
#     # return func
#     return some_func


def static_applier(func: tp.Callable) -> tp.Callable:
    def inner(*args, **kwargs):
        return func(-1, *args, **kwargs)
    return inner


@static_applier
def same(x):
    return x


@static_applier
def get_first(*args):
    return args[0]


print(get_first(1))
# print(get_first(1, 2, 3))


@static_applier
class C:
    def __init__(self, *args):
        self.args = args


a = C(3, 4, 5, 6)

print(a.args)


if hasattr(a, "args"):
    # a.args
    res = getattr(a, "args")
    print(res)


try:
    raise RuntimeError("aaaa")
except IndexError as e:
    print(2)
except RuntimeError as e:
    print(e)
    # raise IndexError("bbb")
    raise

