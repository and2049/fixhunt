class LogDict(dict):
    def __getitem__(self, key):
        print(f'GET {key}')
d = LogDict({'a': 1})
for k, v in d.items():
    _ = d[k]  # triggers PLR1733: logs again; fix would omit log
