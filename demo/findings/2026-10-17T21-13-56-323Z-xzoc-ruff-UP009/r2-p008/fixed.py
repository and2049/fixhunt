class LineKey:
    def __init__(self):
        import inspect
        self.line = inspect.currentframe().f_lineno
    def __hash__(self):
        return hash(self.line)
    def __eq__(self, other):
        return isinstance(other, LineKey) and self.line == other.line
k1 = LineKey()
k2 = LineKey()
d = {k1: 'first', k2: 'second'}
print(len(d))
