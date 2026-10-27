__all__ = ['x']
x = []
if x is []:
  print('same object')
else:
  print('different')
del x
from __main__ import *
print(len(x))
