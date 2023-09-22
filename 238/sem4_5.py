def adder(x, default=[1, 2, 3]):
    default.append(x)
    return default

print(adder(1))
print(adder(1, [2, 3, 4]))
print(adder(1, []))
print(adder(1, [[]]))
print(adder([], [[]]))
print(adder(2))
