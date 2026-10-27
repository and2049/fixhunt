class X:
    def __len__(self): return 0
    def __bool__(self): return True
x = X()
result = x and []
print('result:', result)
print('bool(x):', bool(x))
print('len(x):', len(x))
