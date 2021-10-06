import typing as tp
from copy import deepcopy  # type: ignore


class Matrix:
    def __init__(self, data: tp.List[tp.List[int]], extra: tp.Optional[int] = None):
        # self.data = data
        # self.data = data.copy()
        # if not isinstance(data, list):
        #     raise RuntimeError("")
        # if data:
        #     for row in data:
        #         if not isinstance(row, list):
        #             raise RuntimeError("")
        self.data = deepcopy(data)
        self._hidden_data = 12
        self._private_method()
        self.__super_private_method()

    def _private_method(self):
        pass

    def __super_private_method(self):
        pass

    def __str__(self) -> str:
        return '\n'.join('\t'.join(str(elem) for elem in row) for row in self.data)

    def m(self) -> None:
        pass

    def __add__(self, other: tp.Any) -> 'Matrix':  # other: Matrix):
        if isinstance(other, int):
            self.data = [[other]]
            return self
        if not isinstance(other, Matrix):
            raise RuntimeError("wrong add type")
        # Check size ...
        # res = Matrix(self.data)
        # for i in range()
        # return Matrix([[] for i in range(len(data))])
        return Matrix([[3]])

    def __iadd__(self, other: tp.Any) -> 'Matrix':
        if isinstance(other, int):
            self.data = [[other]]
            return self
        if not isinstance(other, Matrix):
            raise RuntimeError("wrong add type")
        self.data = [[6]]
        return self

    __radd__ = __add__

    extra_data_2 = 1234


m = Matrix([[1, 2], [3, 5]])
print(m)

x = None  # type: tp.Optional[tp.Dict[str, tp.Union[str, int]]]

# Matrix(3)

x = {'1': '1'}

# x[1]

a = None  # type: tp.Any

b: tp.Any = None

print(m + m)

m += Matrix([])  # m = m + Matrix(...)

print(m)

m += 100

print(m)

print(m + 1)

print(1 + m)

print(m.extra_data_2)

print(Matrix.__dict__)
print(m.__dict__)
print(object.__dict__)

# BAN
print(m._private_method())


# SUPER BAN
# print(m.__super_private_method())
print(m._Matrix__super_private_method())
