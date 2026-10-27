class C:
    def __get__(self, obj, owner):
        print('get')
        return 42
    x = __get__()
obj = C()
if not obj.x is 42:
    print('fail')
else:
    print('pass')
