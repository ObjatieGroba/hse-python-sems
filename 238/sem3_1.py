def f(x):
    print(locals())
    p = locals()
    p['y'] = 4
    print(locals())
    def g():
        return p['x'] + p['y']
    return g

get_x = f(1)
get_x2 = f(2)

print(get_x())
print(get_x2())
