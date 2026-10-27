import abc
class MetaABC(type):
  def __new__(mcs, name, bases, ns):
    if abc.ABCMeta not in [type(b) for b in bases]:
      raise RuntimeError('ABCMeta required')
    return super().__new__(mcs, name, bases, ns)
class Base(metaclass=MetaABC):
  pass
class Derived(Base, metaclass=abc.ABCMeta):
  pass
print('ok')
