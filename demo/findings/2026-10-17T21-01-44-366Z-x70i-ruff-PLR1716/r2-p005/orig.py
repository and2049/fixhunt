class SideEffectDict(dict):
    def __missing__(self, key):
        self[key] = key.upper()
        return self[key]
d = SideEffectDict()
if d['a'] == 'A' and d['a'] == 'A':
    print('both equal')
else:
    print('not both equal')
print(d['a'])  # Should be 'A' after first access, but __missing__ ran twice
