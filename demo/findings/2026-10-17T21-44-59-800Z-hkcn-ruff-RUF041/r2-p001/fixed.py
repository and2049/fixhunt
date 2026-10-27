from typing import Literal

def func(a=Literal['x', 'y']):
    a.append('z') if hasattr(a, 'append') else None
    return a

print(func())
print(func())
