import abc
d = {'a': 1, 'b': 2}
class C(metaclass=abc.ABCMeta):
  __hash__ = lambda self: id(self)
  __eq__ = lambda self, other: self is other
  def __setattr__(self, k, v):
    d[k] = v
obj = C()
obj.x = 99
print(d.get('x'))
