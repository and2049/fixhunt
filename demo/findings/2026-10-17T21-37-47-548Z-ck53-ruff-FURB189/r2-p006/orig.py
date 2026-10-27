def f():
    print('f called')
    return dict
class A(f()):  # side effect in base
    pass
print('A.__bases__[0].__name__:', A.__bases__[0].__name__)
a = A()
print('type(a).__name__:', type(a).__name__)
