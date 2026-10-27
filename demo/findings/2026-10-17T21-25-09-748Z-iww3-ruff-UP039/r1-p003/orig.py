class A():
    x: 'B' = None
class B: pass
print(A.__annotations__['x'])
print(B)
