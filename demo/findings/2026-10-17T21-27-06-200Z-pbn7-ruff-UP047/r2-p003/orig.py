from typing import TypeVar
T_co = TypeVar('T_co', covariant=True)
def f(x: T_co) -> T_co:
    return x
class A: pass
class B(A): pass
print(isinstance(f(B()), A))  # Should be True; may break if variance inferred incorrectly
