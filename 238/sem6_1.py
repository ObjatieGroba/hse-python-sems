def func1(x):
    if x == 2:
        raise RuntimeError("X should be not equal 2")
    return 1
        # return None, "X should be not equal 2"
    # return 1, None


def dunc(x):
    func1(x)
    func1(x + 1)
    # res, err = func1(x)
    # if err is not None:
    #     return None, err
    #
    # res, err = func1(x + 1)
    # if err is not None:
    #     return None, err
