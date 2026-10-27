def gen():
    yield 1
    yield 2
s = set(gen())
print(''.join(str(x) for x in s))
