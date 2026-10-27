class Num:
    def __init__(self, n): self.n = n
    def __bool__(self): return self.n != 0
x = Num(0)
if (x):
    print('true')
else:
    print('false')
