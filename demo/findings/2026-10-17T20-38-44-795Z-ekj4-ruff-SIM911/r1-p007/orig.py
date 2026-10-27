class CounterIter:
    def __init__(self, data):
        self.data = data
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= len(self.data):
            raise StopIteration
        result = self.data[self.count]
        self.count += 1
        return result

class DictLike:
    def __init__(self):
        self._keys = ['a', 'b']
        self._vals = [1, 2]
    def keys(self):
        return CounterIter(self._keys)
    def values(self):
        return CounterIter(self._vals)
    def items(self):
        return zip(self._keys, self._vals)

d = DictLike()
print('First zip:', list(zip(d.keys(), d.values())))
print('Second zip:', list(zip(d.keys(), d.values())))  # exhausted
print('Items:', list(d.items()))
