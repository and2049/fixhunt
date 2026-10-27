class A:
    x = 1
    def __get__(self, obj, owner):
        print('get', obj.x if obj else owner)
        return obj.x if obj else 2

def f():
    a = A()
    a.x = 99
    return  # explicit

r = f()
print('returned:', r)
print('a.x:', A().x)
