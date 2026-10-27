def f(*, x=None):
    return [] if x is None else [x]
def g(a, /, b=[]):
    return [a] + b
print(list(f())[0])  # RUF015 trigger
print(list(g(1))[0])  # RUF015 trigger
