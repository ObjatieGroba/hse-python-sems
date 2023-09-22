Переменная = 1

Переменная *= 2
# Same as
# Переменная = Переменная * 2


print(Переменная)

b = str(123)

a = int('123')
c = float('123')

a = False
b = True == True != False
print(b)

a = [1, 2, 3, 'aaa']
a.append(a)
print(a[4][4][1])
print(id(a[4]), id(a))
print(a)


# a = -1
# print(id(a))
# b = -2 + int(input())
# print(id(b))

a = (1, 2, 3)
b = 2
print(b)


class A:
    a = 1

    def __init__(self, b):
        self.b = b

a = A(2)
a.a
a.c = 4
