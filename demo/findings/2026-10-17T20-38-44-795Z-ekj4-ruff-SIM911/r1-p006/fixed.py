d = {'a': 1, 'b': 2}
zipped = d.items()
for k, v in zipped:
    s = f'{k!r}:{v!r}'
    print(s)
# After fix, same output expected
items = d.items()
for k, v in items:
    s = '{!r}:{!r}'.format(k, v)
    print(s)
# Test repr vs str
print(repr(list(zipped)))
print(str(list(items)))
