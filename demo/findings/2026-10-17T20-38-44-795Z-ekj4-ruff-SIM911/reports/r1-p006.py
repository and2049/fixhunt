d = {'a': 1, 'b': 2}
zipped = zip(d.keys(), d.values())
for k, v in zipped:
    s = f'{k!r}:{v!r}'
print(repr(list(zipped)))
