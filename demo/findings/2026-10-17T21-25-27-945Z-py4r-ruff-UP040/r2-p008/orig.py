import typing

class Weird:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return isinstance(other, Weird) and self.val == other.val
    def __repr__(self):
        return f'Weird({self.val})'

# Dict with duplicate keys in construction (later wins)
# But we can't have duplicate keys in dict literal - so build via pairs
pairs = [(Weird(1), 'a'), (Weird(1), 'b'), (Weird(2), 'c')]  # Same hash, equal
D: typing.TypeAlias = dict(pairs)  # Rule triggers here

print(f'D (alias): {D}')
print(f'len(D): {len(D)}')  # Should be 2: {Weird(1): 'b', Weird(2): 'c'}
for k, v in D.items():
    print(f'  {k!r}: {v!r}')

# Test if the dict is mutable and if alias reflects changes
# But alias is the dict object itself
D[Weird(3)] = 'd'
print(f'After adding: {D}')
print(f'len now: {len(D)}')

# Create new dict via alias to see if it's fresh
try:
    new = D()  # This fails - dict is not callable
    print('D() succeeded')
except Exception as e:
    print(f'D() failed: {type(e).__name__}: {e}')

# But we can use it as a type
try:
    y: D = {Weird(4): 'e'}
    print(f'Successfully used D as type annotation: {y}')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
