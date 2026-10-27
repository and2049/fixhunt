class Key:
    def __init__(self, v): self.v = v
    def __hash__(self): return hash(self.v)
    def __eq__(self, other): return isinstance(other, Key) and self.v == other.v
def g() -> Generator[tuple[Key, int], None, None]:
    yield (Key(1), 10)
    yield (Key(2), 20)
d = dict(g())
print(list(d.items()))
