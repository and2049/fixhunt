class C:
    def m(cls):
        return {}
    m = classmethod(m)
d = {'a': 1, 'b': 2}
d[C.m()] = 3
print(d.get('a'), d.get('b'))
