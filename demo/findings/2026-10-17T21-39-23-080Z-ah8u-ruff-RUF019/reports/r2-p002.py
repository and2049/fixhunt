class SideEffectMap:
    def __init__(self):
        self.data = {'x': 1}
        self.calls = 0
    def __contains__(self, key):
        return key in self.data
    def __getitem__(self, key):
        return self.data[key]
m = SideEffectMap()
if 'x' in m and m['x']:
    print(f'second: calls={m.calls}')
