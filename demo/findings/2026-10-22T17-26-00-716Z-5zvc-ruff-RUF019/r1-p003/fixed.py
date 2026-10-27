class BadDict(dict):
    def __getitem__(self, key):
        if key == 'fail':
            raise ValueError('boom')
        return super().__getitem__(key)
d = BadDict({'fail': 0})
try:
    if d.get('fail'):
        print('yes')
except ValueError as e:
    print('ValueError:', e)
finally:
    print('finally ran')
