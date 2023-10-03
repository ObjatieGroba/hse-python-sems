class Vector:
    cdata = [3, 4, 5]

    def __init__(delf, *args):
        delf.data = list(args)
        delf.cdata = delf.cdata.copy()

    def append(self, x):
        self.data.append(x)
        self.cdata.append(x)

    def __repr__(self):
        return f'Vector(args={self.data!r}, cdata={self.cdata!r})'

print(type(Vector))
v = Vector(1)
Vector.append(v, 1)  # v.append(1)
print(v.append, type(v.append))
print(v)


# class DenseVector(Vector):
#     pass


v = Vector(1, 2, 3, 4, 5, 6, 10)

if type(v) == Vector:
    print("v is Vector")
if isinstance(v, Vector):
    print("v is Vector")
print(v)
