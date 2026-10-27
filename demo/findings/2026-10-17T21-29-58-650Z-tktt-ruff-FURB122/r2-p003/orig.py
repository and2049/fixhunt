class T:
    def __init__(self, v): self.v = v
    def __str__(self): return str(self.v)
    def __bool__(self): return self.v > 0
seq = [T(-1), T(0), T(1)]
f = open('tmp.txt', 'w')
for x in seq:
    if x:          # depends on __bool__
        f.write(str(x))
        f.write('T' if x else 'F')
f.close()
print(open('tmp.txt').read())
