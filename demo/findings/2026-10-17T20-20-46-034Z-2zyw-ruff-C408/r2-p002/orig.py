class Desc:
    def __get__(self, obj, owner):
        print('Desc.get')
        return []

class A:
    attr = Desc()

a = A()
print(type(a.attr))
a.attr.append(1)
print(type(A.attr))
