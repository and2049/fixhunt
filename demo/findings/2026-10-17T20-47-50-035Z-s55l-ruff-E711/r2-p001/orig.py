import typing
from typing import get_type_hints
T = typing.TypeVar('T')
def func(x: 'Optional[T]') -> None:
    pass
try:
    hints = get_type_hints(func)
    x = hints['x']
    # This annotation is evaluated at runtime via get_type_hints
    # It contains a string forward-ref that resolves to Optional[T]
    # Now test equality with None inside a context that depends on the resolved type
    val = None
    if x == type(val):  # Rule triggers: compares type(None) == type(None) via ==
        print('equal')
    else:
        print('not equal')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
