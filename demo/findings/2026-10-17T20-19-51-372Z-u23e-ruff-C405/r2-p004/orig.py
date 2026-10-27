class BadDict:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return isinstance(other, BadDict) and self.v == other.v
l = [BadDict(1), BadDict(1)]
s = set(l)
print(f'Set size from duplicate BadDict: {len(s)}')
print(f'Elements: {[x.v for x in s]}')
