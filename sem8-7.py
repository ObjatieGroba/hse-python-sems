class Vector:
    def __init__(self):
        self.data = []

    @staticmethod
    def test():
        print(123)

    def test2(self):
        print(234)

    @property
    def prop(self):
        return [1, 2, 3]

    @prop.setter
    def prop(self, value):
        print("Nothing", value)

    @property
    def prop2(self):
        return self.data

    @prop2.setter
    def prop2(self, value):
        self.data = value


Vector.test()

v = Vector()

v.test()

print(v.test)
print(v.test2)

print(v.prop)

print(Vector.__dict__)

v.prop = [5, 6, 7]


print(v.prop2)

v.prop2 = [7, 7, 7]

print(v.prop2)

print(v.data)

print(locals())
print(globals())
print(globals() is locals())
