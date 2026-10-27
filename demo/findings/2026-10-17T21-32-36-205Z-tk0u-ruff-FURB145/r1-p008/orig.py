class BadList(list):
    def __getitem__(self, key):
        if key == 0:
            raise ValueError('bad')
        return super().__getitem__(key)
    def copy(self):
        return super().copy()
b = BadList([1, 2, 3])
try:
    x = b[:]  # triggers on first element access during slice
    print('slice succeeded:', x)
except ValueError as e:
    print('slice error:', type(e).__name__, str(e))
try:
    y = b.copy()
    print('copy succeeded:', y)
except ValueError as e:
    print('copy error:', type(e).__name__, str(e))
