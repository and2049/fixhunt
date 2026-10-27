class T:
    def __bool__(self): return False
    def __len__(self): return 0
    def __repr__(self): return 'T()'
t = T()
print(f't bool: {bool(t)}')
print(f't len: {len(t)}')
print(f't is None: {t is None}')
print(f't == None: {t == None}')
for i in range(1):
    if t:
        print('truthy')
    else:
        print('falsy')
