d = {}
class Counter:
    def __init__(self):
        self.n = 0
    def __hash__(self):
        self.n += 1
        return id(self)
    def __eq__(self, other):
        return self is other
c1 = Counter()
c2 = Counter()
d[c1] = 'first'
d[c2] = 'second'
trace = []
for k, v in d.items():
    trace.append((k.n, v))
    _ = d[k]  # triggers PLR1733: d[k] re-evaluates __hash__ again
print('trace:', trace)
