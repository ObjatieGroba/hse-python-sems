class Forever:
    def __init__(self, a):
        self.a = a
        # self.elems = tuple(elem for elem in a)
        self.i = iter(a)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.i)
        except StopIteration:
            self.i = iter(self.a)
            return next(self.i)

        # res = self.a[self.i]
        # self.i = (self.i + 1) % len(self.a)
        # return res


def generate111():
    yield 1
    yield 1
    yield 1


for elem in Forever(generate111()):
    print(elem)

# iterator = iter(Forever([1, 2, 3]))
# elem = next(iterator)
# elem = next(iterator)
# elem = next(iterator)
# elem = next(iterator)
# elem = next(iterator)
# elem = next(iterator)
# elem = next(iterator)
# elem = next(iterator)
