log = []
class D(dict):
    def items(self):
        log.append('items')
        return super().items()
    def keys(self):
        log.append('keys')
        return super().keys()
d = D({'a': 1})
for k, v in d.items():
    pass
print(''.join(log))
