class Desc:
    def __get__(self, obj, owner):
        print('Descriptor accessed')
        return None
class A:
    attr = Desc()
a = A()
print(isinstance(a.attr, type(None)))  # Triggers descriptor
print(isinstance(a.attr, type(None)))  # Again
