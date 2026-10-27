import abc
class C(metaclass=abc.ABCMeta):
  '"""doc"""'
  pass
print(C.__doc__)
