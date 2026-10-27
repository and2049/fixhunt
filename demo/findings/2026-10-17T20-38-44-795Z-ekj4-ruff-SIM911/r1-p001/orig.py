class D:
    def __init__(self, n):
        self.n = n
    def keys(self):
        return range(self.n)
    def values(self):
        return range(self.n)
    def items(self):
        return [(i, i) for i in range(self.n)]
    def __bool__(self):
        return self.n > 0
    def __len__(self):
        return self.n

d = D(2)
print('Before:', bool(d))
trace = []
for k, v in zip(d.keys(), d.values()):
    trace.append((k, v))
print('Zip result:', trace)
d.n = 0
print('After zero:', bool(d))
try:
    for k, v in zip(d.keys(), d.values()):
        pass
except Exception as e:
    print('Error:', type(e).__name__, str(e))
