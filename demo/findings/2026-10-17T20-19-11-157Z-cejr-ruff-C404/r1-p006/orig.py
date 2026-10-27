class S:
    def __repr__(self): return "repr"
    def __str__(self): return "str"
s = S()
d = dict([(f'{s}', str(s)) for _ in [1]])
print(repr(d[f'{s}']))
