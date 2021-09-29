# with open('input.txt', 'r') as f:
#     f.seek(10)
#     for line in f.readlines():
#         print(line)
#     f.seek(0)
#     for line in f.readlines():
#         print(line)

def kek(l=[]):
    if isinstance(l, list):
        l.append(1)
    return l


print(kek())
print(kek(1))
print(kek())
