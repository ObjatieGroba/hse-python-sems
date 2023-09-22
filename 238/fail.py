class A:
    f = lambda _: 1

class B:
    def __eq__(self, other):
        other["f"] = lambda _: 2

a = A()
print("before", a.f())

A.__dict__ == B()
print("after", a.f())
