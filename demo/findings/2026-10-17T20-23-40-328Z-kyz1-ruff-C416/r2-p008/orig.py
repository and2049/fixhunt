class IterableObj:
    def __init__(self, data):
        self.data = data
        self.iter_count = 0
    def __iter__(self):
        self.iter_count += 1
        print(f'__iter__ called #{self.iter_count}')
        return iter(self.data)
obj = IterableObj([1, 2, 3])
print('Testing comprehension:')
obj.iter_count = 0
result1 = {x for x in obj}
print(f'Result: {result1}, __iter__ calls: {obj.iter_count}')
obj.iter_count = 0
print('Testing set() constructor:')
result2 = set(obj)
print(f'Result: {result2}, __iter__ calls: {obj.iter_count}')
# To see if set() calls __iter__ more than once, we need to check if it does internal checks
# Some implementations might check isinstance(obj, set) or similar, but set() constructor
# typically just calls __iter__ once. However, let's make it call __iter__ twice by
# having __iter__ return a different iterator each time and checking if we get same results
class DoubleCheckIter:
    def __init__(self, data):
        self.data = data
        self.call_count = 0
    def __iter__(self):
        self.call_count += 1
        print(f'__iter__ call #{self.call_count}')
        if self.call_count == 1:
            return iter(self.data[:])  # First copy
        else:
            return iter(self.data[::-1])  # Reversed on second call
obj2 = DoubleCheckIter([1, 2, 3])
print('\nComprehension with inconsistent __iter__:')
obj2.call_count = 0
try:
    result1 = {x for x in obj2}
    print(f'Result: {sorted(result1)}')
except Exception as e:
    print(f'Error: {e}')
print(f'__iter__ calls: {obj2.call_count}')
obj2.call_count = 0
print('\nset() with same inconsistent __iter__:')
try:
    result2 = set(obj2)
    print(f'Result: {sorted(result2)}')
except Exception as e:
    print(f'Error: {e}')
print(f'__iter__ calls: {obj2.call_count}')
