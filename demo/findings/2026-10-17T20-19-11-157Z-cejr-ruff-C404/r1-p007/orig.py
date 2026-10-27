class Falsy:
    def __len__(self): return 0
    def __bool__(self): return False
f = Falsy()
d = dict([(f, 'yes') for _ in [f] if f])
print('dict:', dict(d), 'len:', len(d))
