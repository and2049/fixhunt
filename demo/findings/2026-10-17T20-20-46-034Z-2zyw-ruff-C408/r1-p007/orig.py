class BadHash:
    def __hash__(self): return 1
    def __eq__(self, o): return isinstance(o, BadHash)
a = BadHash()
b = BadHash()
d = dict([(a, 1), (b, 2)])
print(len(d), sorted(d.items()))
