class C:
    def f():
        return []
    f = staticmethod(f)
result = C().f()
if result:
    print('truthy')
else:
    print('falsy')
print('len:', len(result))
