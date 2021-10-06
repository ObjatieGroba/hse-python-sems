class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.a = 1
        self.__dict__ = self
        # self.a = 1


d = Dict()

d["1"] = 2

print(d)

# print(d.a)

d["abcde"] = 5

print(d.abcde)
