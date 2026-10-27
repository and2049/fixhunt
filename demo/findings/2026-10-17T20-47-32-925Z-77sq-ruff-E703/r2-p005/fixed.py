class C:
  x = 1
  y = x + 1
print(C.x, C.y)
print(hasattr(C, 'z'))  # z not defined
