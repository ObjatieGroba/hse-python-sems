def printer(*args, sep=' ', end='\n', **kwargs):
    print(*args, sep=sep, end=end)
    print(*(sorted(kwargs.items())), sep=sep, end=end)


printer(1, 2, 3, first=1, second=2)

print("=====")

printer(sep='\n', end='\nhello\n', first=1, second=2)


# class MyList(list):
class MyProperties:
    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        while len(self) < value:
            self.append(None)


# a = MyList()
# a = MyProperties()
