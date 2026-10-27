class Descr:
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, objtype=None):
        return getattr(obj, '_' + self.name, None)
    def __set__(self, obj, value):
        setattr(obj, '_' + self.name, value * 2)

class A:
    x = Descr()
    def __init__(self):
        self.x = 5

a = A()
print(a.x)
