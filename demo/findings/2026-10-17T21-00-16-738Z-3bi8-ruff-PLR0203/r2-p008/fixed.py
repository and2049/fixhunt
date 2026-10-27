class C:
    @staticmethod
    def f():
        return []
result = C().f()
if result:
    print('truthy')
else:
    print('falsy')
print('len:', len(result))
