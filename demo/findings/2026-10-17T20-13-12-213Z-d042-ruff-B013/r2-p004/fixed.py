def f(a, /, b, *, c=1):
    return a + b + c
try:
    f(1, 2, c=3)  # works
    raise TypeError
except TypeError as e:
    print(f(4, 5, c=6))
