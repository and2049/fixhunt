def gen():
    x: int = 42
    yield x
print(list(gen()))
