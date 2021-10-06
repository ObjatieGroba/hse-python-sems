class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()

print(isinstance(c, C))
print(isinstance(c, A))
print(isinstance(c, B))
print(isinstance(c, list))

