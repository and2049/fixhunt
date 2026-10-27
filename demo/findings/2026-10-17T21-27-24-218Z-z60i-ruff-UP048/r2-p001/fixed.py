class K:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return isinstance(other, K) and self.v == other.v

m = {}
while True:
    m[K(1)] = 'a'
    m[K(1)] = 'b'  # duplicate key
    break

# Print to show dict size and values (depends on loop having run)
print(len(m))
for k, v in m.items():
    print(f'{k.v}:{v}')
