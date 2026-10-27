class Desc:
    def __get__(self, obj, owner):
        print('Descriptor accessed')
        return None
class A:
    attr = Desc()
a = A()
print((a.attr is None))  # Triggers descriptor
print((a.attr is None))  # Again
