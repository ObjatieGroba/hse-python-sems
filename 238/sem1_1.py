a, b = map(int, input().split())

print(max(a, b))

if a > b:
    print(a)
else:
    print(b)

print(a if a > b else b)

print(a + b - min(a, b))
