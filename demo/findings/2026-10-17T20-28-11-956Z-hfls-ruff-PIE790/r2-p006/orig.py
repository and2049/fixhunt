def f():
    y: int = 'wrong'  # type: ignore  # should be ignored
    ...
    return y
print(f())
