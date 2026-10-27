class Seq:
    def __init__(self, data):
        self.data = list(data)
    def __getitem__(self, key):
        return self.data[key]
    def __len__(self):
        return len(self.data)
    def copy(self):
        raise AttributeError('no copy')
s = Seq([1, 2, 3])
try:
    sliced = s[:]
except TypeError as e:
    sliced = None
    print('slice error:', type(e).__name__, str(e))
try:
    copied = s.copy()
except AttributeError as e:
    copied = None
    print('copy error:', type(e).__name__, str(e))
print('slice result:', type(sliced).__name__ if sliced else 'None')
print('copy result:', type(copied).__name__ if copied else 'None')
