from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import abc
class D(metaclass=abc.ABCMeta):
    x: 'abc.ABC'
    def f(self): return self.x
try:
    d = D()
    d.x = d
    print(d.f().__class__.__name__)
except Exception as e:
    print(f'{type(e).__name__}: {e}')
