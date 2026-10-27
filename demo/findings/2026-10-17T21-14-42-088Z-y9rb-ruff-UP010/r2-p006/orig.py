from __future__ import annotations
def f(a=[]):
    a.append(1)
    return a
print(f())
print(f())
