class BadHash:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return 0
    def __eq__(self, other):
        return isinstance(other, BadHash) and self.val == other.val
d = {BadHash(1): 'a', BadHash(2): 'b'}
for k in list(d):
    print(k.val)
