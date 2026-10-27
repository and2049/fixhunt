class A: pass
class B: pass
a = A()
b = B()
result = setattr(a, 'x', setattr(b, 'y', 1))
print('a.x:', a.x)
print('b.y:', b.y)
print('result:', result)
