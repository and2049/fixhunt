def process(a, /, b, *, c=None):
    if c is None:
        c = b[:]
    c.append(len(b))
    return a, b, c
out = process(1, [2, 3], c=[4])
print('out:', out)
