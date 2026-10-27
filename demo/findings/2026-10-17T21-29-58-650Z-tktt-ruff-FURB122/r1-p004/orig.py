class BadKey:
    def __init__(self, val): self.val = val
    def __hash__(self): return hash(self.val)
    def __eq__(self, other): return self.val == other.val
f = open('tmp.txt', 'w')
d = {BadKey(1): 'a', BadKey(2): 'b'}
for k, v in d.items():
    f.write(f'{k.val}:{v}\n')
f.close()
with open('tmp.txt') as f:
    lines = f.readlines()
print('dict output:', [l.strip() for l in lines])
