def gen():
    x = 10
    yield x
    # Lambda captures x, called after first yield
    f = lambda: x * 2
    yield f()  # Should be 20

print(list(gen()))
