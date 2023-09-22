def gen1():
    print(1)
    yield 1
    print(1)
    yield 1
    print(1)
    yield 1

def gen2():
    print(2)
    yield 2
    print(2)
    yield 2
    print(2)
    yield 2


def gen3():
    yield from gen2()
    yield from gen2()

print(*gen3())


i1 = iter(gen1())
i2 = iter(gen2())
next(i1)
next(i2)
next(i1)
next(i2)