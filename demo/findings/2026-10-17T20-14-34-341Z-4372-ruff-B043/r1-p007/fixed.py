def foo(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
class Container:
    def __init__(self):
        self.data = foo()
c1 = Container()
c2 = Container()
print('c1.data before:', c1.data)
print('c2.data before:', c2.data)
del c1.data
print('c1.data after del:', getattr(c1, 'data', 'missing'))
print('c2.data after:', c2.data)
