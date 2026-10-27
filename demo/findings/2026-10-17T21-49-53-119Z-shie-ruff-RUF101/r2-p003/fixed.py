def f(a, /, b, *, c=eval('1')):  # noqa: S307
    return a + b + c
print(f(10, 20))
try:
    f(10, b=20)
except TypeError as e:
    print('Expected:', e)
