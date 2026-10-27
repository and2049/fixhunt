class WeirdSeq:
    def __init__(self, data, label):
        self.data = list(data)
        self.label = label
    def __add__(self, other):
        # Always returns a fresh list, ignores self
        return list(getattr(other, 'data', [])) if hasattr(other, 'data') else list(other)
    def __iadd__(self, other):
        # Mutates self to be a copy of other
        self.data.clear()
        self.data.extend(getattr(other, 'data', []) if hasattr(other, 'data') else other)
        return self
    def __iter__(self):
        return iter(self.data)
    def __repr__(self):
        return f'WeirdSeq({self.data}, {self.label})'

a = WeirdSeq([1, 2], 'a')
b = WeirdSeq([3, 4], 'b')
c = WeirdSeq([5, 6], 'c')

print('Initial:', a, b, c)
print('\nUsing sum:')
try:
    s = sum([a, b, c], WeirdSeq([], 'start'))
    print('Result:', s)
    print('a,b,c after:', a, b, c)
except Exception as e:
    print('Error:', type(e).__name__, e)

# Reset
a = WeirdSeq([1, 2], 'a')
b = WeirdSeq([3, 4], 'b')
c = WeirdSeq([5, 6], 'c')
print('\nUsing reduce:')
from functools import reduce
import operator
try:
    r = reduce(operator.iadd, [a, b, c], WeirdSeq([], 'start'))
    print('Result:', r)
    print('a,b,c after:', a, b, c)
except Exception as e:
    print('Error:', type(e).__name__, e)
