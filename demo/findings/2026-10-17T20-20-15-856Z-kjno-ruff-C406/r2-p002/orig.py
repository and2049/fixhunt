class Desc:
    def __get__(self, obj, objtype):
        print('desc get')
        return [(1, 2)]

class A:
    x = Desc()

a = A()
try:
    # Access via class triggers descriptor
    result = dict(A.x)
except Exception as e:
    print(type(e).__name__, str(e))
print('done')
