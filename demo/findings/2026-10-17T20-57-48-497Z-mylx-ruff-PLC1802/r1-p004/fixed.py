def h(*, z=None):
  if z is None:
    z = []
  if z:
    z.append(1)
  return z
print(h())
print(h(z=[2]))
