class C:
    @classmethod
    def m(cls):
        return {}
d = {'a': 1, 'b': 2}
d[C.m()] = 3
print(d.get('a'), d.get('b'))
