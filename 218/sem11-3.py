import threading


from queue import Queue


b = 2


def count(res: Queue, l, r):
    global b
    b += 1
    cnt = 0
    for i in range(l, r):
        if i % 2 == 0:
            cnt += 1
    res.put(cnt)
    return cnt


l = 1
r = 10
# print(count(l, r))

res = Queue()

t1 = threading.Thread(target=count, args=(res, l, r // 2))
t2 = threading.Thread(target=count, args=(res, r // 2 + 1, r))
t3 = threading.Thread(target=count, args=(res, r // 2 + 1, r))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# print(res.get() + res.get())
print(res.get())
print(b)
