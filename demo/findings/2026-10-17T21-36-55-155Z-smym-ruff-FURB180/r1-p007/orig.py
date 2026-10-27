import abc
# comment before
class C(metaclass=abc.ABCMeta):  # inline
  x = 1  # field
print(C.x)
