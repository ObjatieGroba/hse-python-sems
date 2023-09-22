class A:
    def __init__(self):
        print("Init")

    def __del__(self):
        print("Del")


a = A()
a = A()
a = A()
print(1)
