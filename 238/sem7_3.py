class Metaclass(type):
    childs = {}

    def __new__(cls, name, bases, dct):
        cls.childs[name] = super().__new__(cls, name, bases, dct)
        return cls.childs[name]

print(__name__)
print(Metaclass.childs)

class Vector(metaclass=Metaclass):
    pass

print(Metaclass.childs)

v = Vector()
print(v)

# print(isinstance(v, Vector))
# print(isinstance(v, object))
# print(isinstance(Vector, object))
# print(isinstance(Vector, type))
# print(isinstance(type, object))
# print(isinstance(object, type))
# print(id(type), id(object))
# print(type)
