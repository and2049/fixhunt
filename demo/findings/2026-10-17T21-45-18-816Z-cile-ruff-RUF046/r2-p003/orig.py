class BadHash:
    def __init__(self, v): self.v = v
    def __hash__(self): return int(5 + 3)
    def __eq__(self, other): return self.v == other.v

d = {BadHash(1): 'a', BadHash(2): 'b'}
print(len(d))
