class C:
    def __init__(self):
        self._count = 0
    @property
    def d(self):
        self._count += 1
        return {'a': 1}
c = C()
print('First access:', end=' ')
if 'a' in c.d.keys():
    print(c._count, end=' ')
print('\nSecond access:', end=' ')
if 'a' in c.d.keys():
    print(c._count)
