def f():
    d = {}
    class K:
        def __init__(self, v): self.v = v
        def __hash__(self): return hash(self.v)
        def __eq__(self, other): return isinstance(other, K) and self.v == other.v
    d[K(1)] = 'a'
    d[K(1)] = 'b'
    return d
print(sorted(f().items()))
