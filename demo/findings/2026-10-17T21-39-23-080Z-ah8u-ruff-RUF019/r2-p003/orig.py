class BadDict(dict):
    def __getitem__(self, key):
        if key == 'x':
            raise ValueError('bad')
        return super().__getitem__(key)
d = BadDict()
try:
    if 'x' in d and d['x']:
        print('yes')
except ValueError as e:
    print(f'caught: {e}')
finally:
    print('finally')
