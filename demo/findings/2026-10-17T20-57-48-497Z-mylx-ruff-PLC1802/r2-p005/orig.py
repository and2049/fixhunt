class Weird:
    def __len__(self): return 1
    def __bool__(self): return False

w = Weird()
print('len(w):', len(w))
print('bool(w):', bool(w))
if len(w):
    print('len truthy')
else:
    print('len falsy')
