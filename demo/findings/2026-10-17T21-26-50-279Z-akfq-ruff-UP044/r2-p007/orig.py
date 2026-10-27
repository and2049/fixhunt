from typing import Unpack, get_type_hints
def f(*args: 'Unpack[tuple[int, ...]]') -> None:
    pass
hints = get_type_hints(f)
print(hints.get('args', 'missing'))
