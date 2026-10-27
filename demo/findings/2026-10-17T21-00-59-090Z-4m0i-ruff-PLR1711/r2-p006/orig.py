class C:
    def __bool__(self): return False
    def __len__(self): return 1

def f():
    c = C()
    return

obj = f()
if obj is None:
    print('is None')
else:
    print('not None')
if obj == None:
    print('== None')
else:
    print('!= None')
if obj:
    print('truthy')
else:
    print('falsy')
