class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = 0

    def data(self):
        self.data += 1
        print("Impossible")

    def test(self):
        print("I am test")


def other_test(self):
    print("I am other test")


print(Dict.__dict__)

d = Dict()
print(type(d.__dict__))
print(d.__dict__)
print(d.__dict__["data"])

Dict.data(d)

print(d.__dict__["data"])

# Dict.data(1)

d.test()

test_copy = d.test

print(test_copy)

Dict.test = other_test

d.test()

print(d.__dict__)

d.test = test_copy

print(d.__dict__)

d.test()
