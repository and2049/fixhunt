def gen():
  yield 1
  yield 2
g = gen()
if g == []:
  print('unreachable')
else:
  print('not list')
first = list(g)
second = list(g)
print(len(first), len(second))
