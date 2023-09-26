import time


class MyException(Exception):
    pass

def func():
    raise MyException("aaa")

print(1)
try:
    func()
except ValueError:
    print(2)
except Exception as e:
    print(e)
    time.sleep(500)
    # raise RuntimeError("Again") from e
    raise

