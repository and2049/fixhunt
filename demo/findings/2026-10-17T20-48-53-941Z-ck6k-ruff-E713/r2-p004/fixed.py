class BadHash:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return self.v == other.v
s = {BadHash(1), BadHash(1), BadHash(2)}  # dedup by hash/eq
print(BadHash(1) not in s)
print(BadHash(3) not in s)
d = {BadHash(1): 'a', BadHash(2): 'b'}
print(BadHash(1) not in d)
print(BadHash(3) not in d)
