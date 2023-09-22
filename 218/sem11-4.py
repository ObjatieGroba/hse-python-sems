import multiprocessing


b = 2


def count(r):
    global b
    b += 1
    cnt = 0
    for i in range(0, r):
        if i % 2 == 0:
            cnt += 1
    return cnt


p = multiprocessing.Pool(5)
print(p.map(count, (10 for i in range(100))))
print(b)
