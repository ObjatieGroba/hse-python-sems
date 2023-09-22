# import sem8
#
#
# print(sem8.Array([2, 3, 4]))


class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def __hash__(self):
        return len(self)

    # def __eq__(self, other):
    #     return self == other


class Dict2(Dict):
    pass


class A:
    pass


# print(isinstance(1, object))

# d = Dict(((1, 2), (3, 4)))
d = Dict()

d[A()] = 1

d["1"] = 1
print(d)

d["d"] = d

d[d] = 2

print(d)

print(d[d])

