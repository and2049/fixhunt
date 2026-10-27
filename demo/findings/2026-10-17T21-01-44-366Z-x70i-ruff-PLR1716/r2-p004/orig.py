class Desc:
    def __init__(self, val):
        self.val = val
    def __get__(self, obj, objtype):
        self.val += 1
        return self.val
class A:
    x = Desc(0)
a = A()
if a.x < 2 and a.x < 3:
    print(a.x.val)
else:
    print(0)
