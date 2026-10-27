import abc
bases = ()
cls = type('Dynamic', bases, {'metaclass': abc.ABCMeta})
try:
  cls()
except TypeError as e:
  print('TypeError:', type(e).__name__, str(e))
