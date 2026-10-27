def g():
  x = [1, 2, 3]
  if len(x) == 3:
    return sum(x)
  return 0
print(g())
x = [1, 2]
if len(x) == 3:
  print('no')
else:
  print(len(x))
