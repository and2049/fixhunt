class SetLike:
    def __init__(self):
        self._data = {1, 2}
    def __iter__(self):
        return iter(self._data)
    def __bool__(self):
        return len(self._data) > 0
    def __len__(self):
        return len(self._data)
    def discard(self, x):
        self._data.discard(x)
s = SetLike()
for x in s:
    s.discard(x)
print('remaining:', list(s._data))
