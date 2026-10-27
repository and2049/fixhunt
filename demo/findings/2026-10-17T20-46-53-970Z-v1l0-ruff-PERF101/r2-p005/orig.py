def gen():
    yield 1
    yield 2
    yield 3
it = gen()
out = []
for x in list(it):
    out.append(x)
    try:
        next(it)
    except StopIteration:
        pass
print(out)
