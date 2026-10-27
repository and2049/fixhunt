class StrLen:
    def __init__(self, s): self.s = s
    def __len__(self): return len(self.s)
    def __bool__(self): return bool(len(self.s))
x = StrLen('')
y = StrLen('nonempty')
print('x is False:', x is False)
print('x == False:', x == False)
print('bool(x):', bool(x))
print('bool(y):', bool(y))
