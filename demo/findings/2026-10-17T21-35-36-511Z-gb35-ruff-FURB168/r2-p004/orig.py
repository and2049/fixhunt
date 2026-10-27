def f(*, x=[]):
    isinstance(x.pop() if x else None, type(None))
    return len(x)
print(f())  # First call
print(f())  # Second call, x is same list
