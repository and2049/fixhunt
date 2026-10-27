class Obj:
    def __str__(self): return 'str'
    def __repr__(self): return 'Obj()'
o = Obj()
assert False, print(o)
try:
    assert False
except AssertionError as e:
    print('Message:', e)
