class K:
    def __init__(self, v):
        self.v = v
    def __hash__(self):
        return hash(self.v)
    def __eq__(self, other):
        return isinstance(other, K) and self.v == other.v

d = {K(1): 'a', K(1): 'b', K(2): 'c'}  # duplicate key
print('Dict:', d)
trace_keys = list(d.keys())
trace_vals = list(d.values())
trace_items = list(d.items())
print('Keys:', [k.v for k in trace_keys])
print('Values:', trace_vals)
print('Items:', [(k.v, v) for k, v in trace_items])
zipped = list(zip(d.keys(), d.values()))
print('Zipped:', [(k.v, v) for k, v in zipped])
if zipped != list(d.items()):
    print('MISMATCH')
