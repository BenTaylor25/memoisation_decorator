# Memoization Decorator

```py
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
```

Memoization is an optimisation strategy
for stateless functions that are often
called with the same inputs, which
involves caching return values to
skip expensive calculations.

Or in English:
- If you have a function that always
gives the same output for a given input
(e.g. `add_one(4)` should always return `5`),
- But the function takes a long time to
execute (e.g. `get_nth_prime(n)`),
- If there's a chance you might need to
call the function multiple times with the
same input value,
- You can keep track of the inputs you have
already solved, and skip the long calculation.

Memoization is usually implemented using
a Hash Table / Dictionary, as they have very
fast access speeds for large quantities.

Usually, you would implement memoization
manually for every function, which results in
bloated functions.  
As the steps to implement memoization are
always the same, this is a suitable use case
for Python's function decorators.

Function decorators are functions that modify
other functions, usually to do something
additional before / after typical behaviour.  
E.g. you could use a decorator to make a
function print its return value:
```py
def output(func):
    def wrapper():   # create a new function
        rv = func()   # use the old function
        print(rv)   # add some new behaviour
    return wrapper   # return the new function

def return_five():
    return 5

# replace the old function with the new function
return_five = output(return_five)

return_five()   # prints 5 to the screen
```

Typically, decorators use the following
syntactic sugar which is equivalent:
```py
@output   # decorate the following function
def return_five():
    return 5
```
We also usually want to make decorators
dynamic, which we can do with args and
kwargs.


*See also: args, kwargs, caching, dicts,
higher-order functions, Python typing.*
