from time import sleep
from timer import timer
from memoisation_decorator import memoize


@timer
def slow_add_one(x: int):
    sleep(3)
    return x + 1

@timer
@memoize
def memo_slow_add_one(x: int):
    sleep(3)
    return x + 1

def test_one():
    print("no memoization")
    print("--------------")
    slow_add_one(1)   # takes 3 seconds
    slow_add_one(1)   # takes 3 seconds

    print()

    print("memoization")
    print("-----------")
    memo_slow_add_one(1)   # takes 3 seconds
    memo_slow_add_one(1)   # runs instantly

    print()


@memoize
def _fibonacci(n: int):
    # Maximum recursion depth gets reached
    # before performance is noticeable...
    sleep(0.1)

    if n <= 1:
        return n
    else:
        return _fibonacci(n - 1) + _fibonacci (n - 2)

@timer
def fibonacci(n: int):
    return _fibonacci(n)

def test_two():
    print("fibonacci")
    print("---------")

    fibonacci(20)   # ~2.3 seconds
    fibonacci(25)   # ~0.5 seconds, even though it's bigger


if __name__ == "__main__":
    test_one()
    test_two()