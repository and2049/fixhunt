class BadKey:
    def __init__(self, val): self.val = val
    def __hash__(self): return hash(self.val)
    def __eq__(self, other):
        # Simulate hash collision drift
        return self.val == other.val and hasattr(self, '_eq_count') and self._eq_count < 2

d = {}
k1 = BadKey(1)
k2 = BadKey(1)  # Same hash, potentially eq
d[k1] = 'first'
d[k2] = 'second'  # Overwrites if __eq__ says equal

items = list(d.items())
for pos, (k, v) in enumerate(items):
    # Rule triggers on d[k] -> should become v
    print(f'd[{k.val}] via index: {d[k]}, via loop: {v}')
