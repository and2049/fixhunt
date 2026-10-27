class K:
    def __init__(self, v): self.v = v
    def __eq__(self, other): return isinstance(other, K) and self.v == other.v
    def __hash__(self): return hash(self.v)
d1 = {K(1): 'a', K(1): 'b'}  # deduped to one
d2 = {'x': 1, 'y': 2}
try:
    res = list(map(lambda kv: kv[0].v + kv[1], zip(d1.items(), d2.items())))
    print('result:', res)
except Exception as e:
    print('error:', type(e).__name__, str(e))
