_ = int(input())
t = list(map(int, input().split()))

s = 0
for i in t:
    s += i
print(s)

print(sum(t))

s = 0
for i in range(len(t)):
    s += t[i]
print(s)
