from time import perf_counter

def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        rv = func(*args, **kwargs)
        end = perf_counter()
        print(f"{rv} ({end - start:.1f} seconds)")
        return rv
    return wrapper
