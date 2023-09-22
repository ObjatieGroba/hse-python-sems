class Array:
    def __init__(self, l=None):
        self.data = []
        if l is not None:
            # if type(l) != list:
            # if type(l) is not list:
            if not isinstance(l, list):
                raise RuntimeError(f"Not valid type for arg l: {l!r}")
            self.data = l

    def __str__(self):
        return ', '.join(map(str, self.data))

    def __repr__(self):
        return f"Array({self.data!r})"

    # def data(self):
    #     pass

    def append(self, elem):
        self.data.append(elem)

    def reverse(self):
        # self.data = list(reversed(self.data))
        # self.data.reverse()

        # self = Array(list(reversed(self.data)))

        # self.data_copy = self.data.copy()
        self.data.reverse()


a = Array()

# print(a.data_copy)

# print(Array)
# print(type(a))

# print(a.__dict__)
# print(a.__getattribute__("data"))

a.data.append(1)
# a.data()

a.append(2)

print(a)

print(repr(a))

a.reverse()

# print(a.data_copy)

print(a)

# a.abcd = 2
#
# print(a.abcd)

#
# print(a)
#
# print(repr(a))

