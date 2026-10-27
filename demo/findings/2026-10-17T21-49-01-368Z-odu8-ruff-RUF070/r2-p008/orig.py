def gen():
    while (x := next(it)) != 0:
        yield x
it = iter([3, 2, 1, 0])
print(list(gen()))
