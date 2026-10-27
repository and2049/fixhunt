class Key:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return self.val == other.val
k1 = Key(1)
k2 = Key(1)
d = {k1: 'first', k2: 'second'}
items = list(d.items())[:]
print('dict len:', len(d), 'slice len:', len(items))
for k, v in items:
    print(k.val, v)
