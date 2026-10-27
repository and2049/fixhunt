class BadKey:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return self.v == other.v
try:
    d = {BadKey(1): 'a', BadKey(2): 'b'}
    raise ValueError('collision')
except ValueError as v:
    d[BadKey(1)] = v
    raise v
print(d)
