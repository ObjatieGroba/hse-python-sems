def req_stat(func):
    cur = 0
    cmax = 0
    def inner(*args):
        nonlocal cur, cmax
        if cur == 0:
            cmax = 0
        cur += 1
        cmax = max(cmax, cur)
        res = func(*args)
        cur -= 1
        if cur == 0:
            print(cmax)
        return res
    return inner

@req_stat
def req(x):
    if x == 0 or x == 1:
        return 0
    return req(x - 1) + req(x - 2)

@req_stat
def req2(x):
    if x == 0 or x == 1:
        return 0
    return req(x - 1) + req2(x - 2)

req2(10)
# print(req.max)
