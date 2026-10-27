def f():
  import abc
  class Local(metaclass=abc.ABCMeta):
    pass
  return Local()
print(type(f()))
