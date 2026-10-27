class A(dict):
    pass
print('bases:', A.__bases__)
print('mro:', [c.__name__ for c in A.__mro__])
x = A()
print('type(x).__name__:', type(x).__name__)
