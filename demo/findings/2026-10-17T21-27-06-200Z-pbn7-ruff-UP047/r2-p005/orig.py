from typing import TypeVar
T = TypeVar('T')
def f(x: T) -> T:
    return x
def g(y: T) -> str:  # Reuses T from module scope
    return f(y)
print(g(42))
