def f(*, x=[]):
    (x.pop() if x else None) is None
    return len(x)
print(f())  # First call
print(f())  # Second call, x is same list
