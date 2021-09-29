import time


def cacher(func):
    cache = {}
    def inner(*args):
        print("Inner", *args)
        if args in cache:
            print("Cached", *args)
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return inner


# g = cacher(g)
@cacher
def g(x):
    print("Call", x)
    if x == 0 or x == 1:
        return 1
    return g(x - 1) + g(x - 2)


start = time.time()
print(g(30))
print(time.time() - start)


print(g(30))


import requests


def api(func):
    def inner(*args):
        return requests.get("http://yandex.ru", data=str(args))
    return inner


@api
def method(x, y):
    pass


def method(x, y):
    return requests.get("http://yandex.ru", data=str(x, y))
def method2(x, y):
    return requests.get("http://yandex2.ru")
def method3(x, y, z):
    return requests.get("http://yandex2.ru", data=str(x, y, z))
def method4(x, y):
    return requests.get("http://yandex2.ru")
def method5(x, y):
    return requests.get("http://yandex2.ru")

