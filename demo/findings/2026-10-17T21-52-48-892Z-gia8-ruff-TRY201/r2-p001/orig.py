def f(x=[]):
    try:
        x.append(1)
        raise ValueError('bad')
    except ValueError as exc:
        raise exc
print(f())
print(f())
