def f():
    d = {'a': 1}
    for k, v in d.items():
        pass
    try:
        print(v)
    except NameError as e:
        return f'{type(e).__name__}: {e}'
print(f())
