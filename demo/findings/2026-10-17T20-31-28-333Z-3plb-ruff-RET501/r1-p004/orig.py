def f():
    return None  # explicit for clarity; avoids tuple perception

g = lambda: None
print('f() is g():', f() is g())
print('type(f()):', type(f()))
print('f().__class__:', f().__class__)
