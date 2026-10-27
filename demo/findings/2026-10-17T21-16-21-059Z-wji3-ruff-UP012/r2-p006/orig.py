
class BadKey:
    def __init__(self, val): self.val = val
    def __hash__(self): return hash(self.val)
    def __eq__(self, other): return self.val == other.val

k1 = BadKey('a')
k2 = BadKey('a')  # same hash, equal
d = {}
d[k1.encode('utf-8')] = 'first'  # UP012 triggers on k1.encode()
d[k2.encode('utf-8')] = 'second'  # second triggers too
print(f'{len(d)} {list(d.values())}')
if len(d) == 1:
    print('keys collided')
else:
    print('keys separated')
