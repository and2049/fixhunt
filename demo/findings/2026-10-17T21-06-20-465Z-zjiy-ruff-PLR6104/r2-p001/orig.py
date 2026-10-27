class A:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return A(self.v + other.v)
    def __iadd__(self, other):
        self.v *= 2
        return self

a = A(1)
b = a
a = a + A(1)
print('plain:', a.v, id(a))
print('alias:', b.v, id(b))
