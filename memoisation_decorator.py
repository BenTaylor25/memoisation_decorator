from types import FunctionType

def memo_key(*args, **kwargs) -> str:
    """
    I feel like this function can be hacked,
    but I've tried a few inputs and Python
    correctly distinguished them.

    e.g.
    memo_key('hello', 5, 'world', 1)          => ('hello', 5, 'world', 1){}
    !=
    print(memo_key("hello', 5, 'world", 1))   => ("hello', 5, 'world", 1){}

    Please submit a PR if you can think of
    a better key, but this isn't the
    point of this repo
    """
    return repr(args) + repr(kwargs)

def memoize(func: FunctionType) -> FunctionType:
    memo = {}
    def m_func(*args, **kwargs):
        key = memo_key(*args, **kwargs)
        if key in memo:
            return memo[key]
        rv = func(*args, **kwargs)
        memo[key] = rv
        return rv
    return m_func


if __name__ == "__main__":
    print(memo_key('hello', 5, 'world', 1))
    print(memo_key("hello', 5, 'world", 1))

    print(memo_key({'a': 4, 'b': 5}) == memo_key({'b': 5, 'a': 4}))
