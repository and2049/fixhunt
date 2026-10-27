class LogList(list):
    def __init__(self, data, name):
        super().__init__(data)
        self.name = name
    def __add__(self, other):
        print(f'add {self.name} + {getattr(other, "name", "?")}')
        return super().__add__(other)
    def __iadd__(self, other):
        print(f'iadd {self.name} += {getattr(other, "name", "?")}')
        return super().__iadd__(other)

lst1 = LogList([1], 'A')
lst2 = LogList([2], 'B')
lst3 = LogList([3], 'C')
print('sum:')
result = sum([lst1, lst2, lst3], [])
print('reduce-like:')
# Manual reduce for comparison
from functools import reduce
import operator
result2 = reduce(operator.iadd, [lst1, lst2, lst3], [])
print('Results equal:', result == result2)
