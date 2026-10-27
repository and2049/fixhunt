buf = []
class B:
    def __init__(self, v): self.v = v
    def __radd__(self, other): buf.append('radd'); return self.v.decode() + other
    def __iadd__(self, other): buf.append('iadd'); self.v += other.encode(); return self
x = B(b'a')
x = x + b'b'
print(''.join(buf), x.v)
# Trigger: x = x + b'b' -> x += b'b'
