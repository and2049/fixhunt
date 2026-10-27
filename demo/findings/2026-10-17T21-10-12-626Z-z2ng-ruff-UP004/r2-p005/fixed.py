class Key:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return isinstance(other, Key) and self.val == other.val

k1 = Key(1)
k2 = Key(1)
d = {k1: 'first', k2: 'second'}
print(len(d), d[k1])
