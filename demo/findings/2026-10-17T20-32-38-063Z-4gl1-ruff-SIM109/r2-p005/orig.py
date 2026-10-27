class Obj:
    def __getattr__(self, name):
        Obj.count += 1
        return 42
Obj.count = 0
o = Obj()
if o.prop == 42 or o.prop == 42:
    pass
print('Attribute accesses:', Obj.count)
