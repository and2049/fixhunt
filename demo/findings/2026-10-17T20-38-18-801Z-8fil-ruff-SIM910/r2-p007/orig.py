class Obj:
    def __bool__(self): return False
    def __repr__(self): return 'Obj()'
d = {'k': Obj()}
v = d.get('k', None)
print('v is None:', v is None, 'v == None:', v == None, 'bool(v):', bool(v))
v2 = d.get('missing', None)
print('v2 is None:', v2 is None, 'v2 == None:', v2 == None, 'bool(v2):', bool(v2))
