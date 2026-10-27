import abc
def outer():
  class Inner(abc.ABC):
    __classcell__ = None
    def method(self):
      return 42
  return Inner()
print(outer().method())
