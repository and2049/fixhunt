import abc
from inspect import isabstract
@abc.abstractclassmethod
    def amethod(cls): pass
@classmethod
@abc.abstractmethod
    def bmethod(cls): pass
print('amethod isabstract:', isabstract(amethod))
print('bmethod isabstract:', isabstract(bmethod))
print('amethod.__isabstractmethod__:', getattr(amethod, '__isabstractmethod__', 'missing'))
print('bmethod.__isabstractmethod__:', getattr(bmethod, '__isabstractmethod__', 'missing'))
