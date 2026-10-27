class BadHash:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return isinstance(other, BadHash) and self.v == other.v
d = {BadHash(1): 'a', BadHash(2): 'b'}
k = BadHash(1)
if k in d or k == BadHash(2):
    print('found via dict or equality')
else:
    print('not found')
