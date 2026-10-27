class BadHash:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return self.v == other.v
obj = type('O', (), {})()
k = BadHash(1)
setattr(obj, k, 'val')  # set via setattr with object key
delattr(obj, k)  # triggers rule: attr name is str(k) -> '1'
print('remaining:', list(obj.__dict__.keys()))
