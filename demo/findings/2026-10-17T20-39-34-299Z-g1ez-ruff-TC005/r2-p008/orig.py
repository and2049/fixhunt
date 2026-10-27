import typing
d = {}
if typing.TYPE_CHECKING:
    pass
d['a'] = 1
d['b'] = 2
d['a'] = 3  # duplicate key
for k, v in d.items():
    print(f'{k}:{v}', end=' ')}
print()
