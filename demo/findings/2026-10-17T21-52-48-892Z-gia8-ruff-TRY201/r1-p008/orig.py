class HashExc(Exception):
    def __init__(self, val):
        self.val = val
        super().__init__(str(val))
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return isinstance(other, HashExc) and self.val == other.val
try:
    exc = HashExc(42)
    raise exc
except HashExc as e:
    d = {e: 'found'}
    print(d.get(e, 'missing'))
    raise e
