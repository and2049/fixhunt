class DictHolder:
    def __init__(self):
        self.d = {'a': 1}
    @property
    def keys(self):
        return self.d.keys()
    @property
    def values(self):
        self.d = {'b': 2}
        return self.d.values()
h = DictHolder()
k, v = zip(h.keys, h.values)
print(list(k), list(v))
