class K:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return isinstance(other, K) and self.v == other.v

def f():
    d = {K(1): 'a', K(1): 'b'}  # duplicate key
    return  # explicit

r = f()
print('returned:', r)
print('dict built?')
