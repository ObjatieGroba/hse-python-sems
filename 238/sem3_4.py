def get_default_if_empty(*args, default=None):
    global prev
    if args:
        prev = list(args)
    elif default is not None:
        prev = default
    return prev

print(get_default_if_empty(1, 2, 3))
print(get_default_if_empty())
print(get_default_if_empty(default=[2, 2, 3]))
