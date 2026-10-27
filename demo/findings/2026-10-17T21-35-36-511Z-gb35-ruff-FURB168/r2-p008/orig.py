class Z:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return self.val == other.val
d = {}
z1 = Z(1)
z2 = Z(1)
d[z1] = 'first'
d[z2] = 'second'  # Same hash, equal -> overwrites
for k in d:
    print(isinstance(d[k], type(None)), end=' ')  # Should be False twice
print()
