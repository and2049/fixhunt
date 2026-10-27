from typing import TypeVar
T = TypeVar('T')
def f(x):
    return x.__annotations__['x']  # Accesses annotation at runtime
try:
    result = f(1)
except NameError as e:
    print('NameError:', e)
