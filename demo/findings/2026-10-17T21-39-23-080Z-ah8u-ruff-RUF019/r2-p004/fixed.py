d = {'x': 42}
access_count = 0
class CountingDict(dict):
    def __getitem__(self, key):
        nonlocal access_count
        access_count += 1
        return super().__getitem__(key)
d = CountingDict({'x': 42})
if d.get('x'):
    val = d['x']
    print(f'value: {val}, accesses: {access_count}')
