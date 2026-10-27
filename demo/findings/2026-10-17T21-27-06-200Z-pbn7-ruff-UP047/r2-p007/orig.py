from typing import TypeVar
T = TypeVar('T')
def identity(x: T) -> T:
    return x
def wrapper(x: T) -> T:  # Still uses module T
    return identity(x)
print(wrapper('test'))  # May fail if identity is rewritten but wrapper not
