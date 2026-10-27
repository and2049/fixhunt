class Buf:
    def __init__(self): self.data = []
    def write(self, s): self.data.append(s)
    def __iadd__(self, other): self.write(other); return self
    def __enter__(self): return self
    def __exit__(self, *a): pass
with Buf() as b:
    b = b + 'x'  # Trigger
    print(len(b.data))
# After: b += 'x' still calls write once, but if __iadd__ were chained...
