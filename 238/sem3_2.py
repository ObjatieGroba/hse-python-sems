def process(x):
    return x

def decorator(f):
    def inner(x):
        return f(x) + 2
    return inner

@decorator
def new_process(x):
    return x + 2

process = decorator(process)

print(new_process(1))
