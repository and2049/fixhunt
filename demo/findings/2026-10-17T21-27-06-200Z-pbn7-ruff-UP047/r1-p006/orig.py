from typing import TypeVar
T = TypeVar('T')
def func(x: 'T') -> T:  # type: ignore
    return x
print(func("test"))
