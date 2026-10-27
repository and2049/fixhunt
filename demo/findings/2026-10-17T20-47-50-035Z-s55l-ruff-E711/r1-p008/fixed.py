class Validator:
    def __get__(self, obj, objtype):
        print('get called')
        return getattr(obj, '_x', None)
class MyClass:
    x = Validator()
    def __init__(self):
        self._x = None
obj = MyClass()
print(obj.x == None)
