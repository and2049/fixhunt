def f():
    try:
        raise ValueError
    except (ValueError,):
        return 42
print(f())
