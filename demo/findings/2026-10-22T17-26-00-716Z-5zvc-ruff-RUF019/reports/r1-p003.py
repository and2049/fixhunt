class BadDict(dict):
    def __getitem__(self, key):
            raise ValueError('boom')
d = BadDict({'fail': 0})
try:
    if 'fail' in d and d['fail']:
        print('yes')
except ValueError as e:
    print('finally ran')
