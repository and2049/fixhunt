def f(x=[]):
    x.append(1)
    return x
class A:
    b = f()
print(A.b)
A2 = A()
print(f())
