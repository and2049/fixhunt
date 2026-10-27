def f(x):
    print('f', x)
    if x == 2:
        raise ValueError('bad')
    return x > 0
try:
    any(list(f(x) for x in [0, 1, 2, 3]))
except ValueError as e:
    print('ValueError:', e)
