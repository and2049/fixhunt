class BadKey:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        print(f'hash({self.val})')
        return hash(self.val)
    def __eq__(self, other):
        return isinstance(other, BadKey) and self.val == other.val

keys = [BadKey(1), BadKey(2), BadKey(1)]  # note: duplicate logical key
d = {k: k.val*10 for k in keys}
for i, k in enumerate(keys):
    _ = d[k]  # original: re-hashes k each time
print('done')
