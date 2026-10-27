def f():
  import abc
  class Local(abc.ABC):
    pass
  return Local()
print(type(f()))
