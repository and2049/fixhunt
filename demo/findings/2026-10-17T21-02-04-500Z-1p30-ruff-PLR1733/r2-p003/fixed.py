class Mapping:
    def __init__(self):
        self.data = {'a': 1}
        self.log = []
    def __getitem__(self, k):
        self.log.append(k)
        return self.data[k]
    def items(self):
        return self.data.items()

m = Mapping()
for k, v in m.items():
    print(v)  # triggers __getitem__, logs 'a'
print('log:', m.log)
