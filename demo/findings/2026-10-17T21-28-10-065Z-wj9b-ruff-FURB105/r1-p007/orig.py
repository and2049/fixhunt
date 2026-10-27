class Key:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return self.v == other.v
d = {Key(''): 1, Key(''): 2}
print(len(d))
print('', sep='')
