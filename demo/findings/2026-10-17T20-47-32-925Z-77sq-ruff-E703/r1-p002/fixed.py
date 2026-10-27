class C:
  attr = []
def f():
  C.attr.append(1)
f()
f()
print(C.attr)
