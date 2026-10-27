def gen():
    if (x := 5) > 0:
        yield x
print(list(gen()))
