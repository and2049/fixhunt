from typing import TypeVar
T = TypeVar('T')
def f(x: T) -> 'list[T]':  # String annotation uses T
    return [x]
print(f(1))
