class Key:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return self.v == other.v
d = {}
k1 = Key(1)
k2 = Key(1)
d[k1] = 'first'  #
d[k2] = 'second'  #
print(len(d), d[k1])
