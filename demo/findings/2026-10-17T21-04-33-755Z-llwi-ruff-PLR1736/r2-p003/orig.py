class Bag:
    def __init__(self):
        self._data = [5, 6, 7]
        self.count = 0
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, v):
        self.count += 1
        self._data = v

b = Bag()
for i, x in enumerate(b.data):
    b.data[i] = x + 1  # triggers setter each time!
print(f'setter called {b.count} times')
