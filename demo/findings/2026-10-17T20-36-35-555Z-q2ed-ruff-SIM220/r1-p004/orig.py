class Dict:
    def __init__(self):
        self.store = {'k': 1}
        self.log = []
    def __getitem__(self, key):
        self.log.append(key)
        return self.store[key]
d = Dict()
result = d['k'] and not d['k']
print('result:', result, 'log:', d.log)
