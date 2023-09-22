a = input()
b = input()

for i in range(len(a)):
    print(a[i], b[i], sep='', end='')
print()

s = ''
for i in range(len(a)):
    s += a[i]
    s += b[i]
print(s)
