def gen():
    yield from ['0b1010', '0b1111']
g = gen()
vals = []
for s in g:
    v = int(s[2:], 2)
    vals.append(v)
    if len(vals) == 1:
        # Second pass over same generator - now exhausted
        second = [int(x[2:], 2) for x in g]
print('First pass:', vals)
print('Second pass:', second)
