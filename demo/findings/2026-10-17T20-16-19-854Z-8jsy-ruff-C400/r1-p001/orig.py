class Key:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        print('eq', self.v)
        return isinstance(other, Key) and self.v == other.v
items = [Key(1), Key(1)]
gen = ((k, k.v) for k in items)
d = dict(list(gen))
print(len(d))
