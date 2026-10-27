class LogDict(dict):
    def __getitem__(self, key):
        print(f'GET {key}')
        return super().__getitem__(key)
d = LogDict({'a': 1})
trace = []
for k, v in d.items():
    trace.append(v)
    _ = d[k]  # triggers PLR1733: logs again; fix would omit log
print('trace:', trace)
