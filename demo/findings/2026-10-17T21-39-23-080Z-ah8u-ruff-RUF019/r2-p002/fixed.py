class SideEffectMap:
    def __init__(self):
        self.data = {'x': 1}
        self.calls = 0
    def __contains__(self, key):
        return key in self.data
    def __getitem__(self, key):
        self.calls += 1
        if key not in self.data:
            raise KeyError(key)
        return self.data[key]
m = SideEffectMap()
if m.get('x'):
    print(f'first: calls={m.calls}')
if m.get('x'):
    print(f'second: calls={m.calls}')
print(f'total calls: {m.calls}')
