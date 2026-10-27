lst = [1, 2, 3]
# Rule triggers on: not x in lst
f = lambda x: not x in lst
print('lambda(0):', f(0))
print('lambda(2):', f(2))
print('list comp:', [f(i) for i in range(4)])
