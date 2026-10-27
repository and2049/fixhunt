class Vec:
    def __init__(self, x):
        self.x = x
    def __hash__(self):
        return hash(tuple(self.x))
    def __eq__(self, other):
        return isinstance(other, Vec) and tuple(self.x) == tuple(other.x)
a = Vec([1, 2])
b = Vec([1, 2])
d = {tuple([a.x]): 'first', list(tuple([b.x])): 'second'}
print(f'Dict length: {len(d)}')
for k, v in d.items():
    print(f'{k}: {v}')
