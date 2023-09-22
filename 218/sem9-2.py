class Timer:
    def __enter__(self) -> object:
        return 1

    def __exit__(self, exc_type: type, exc_val: Exception, exc_tb) -> bool:
        print("exit", exc_type, exc_val, exc_tb)
        return True


print("before")

with Timer() as timer:
    # raise RuntimeError("123")
    print(timer)

print("after")

# print(timer)
