from typing import Optional

def func(x: Optional[int]) -> bool:
    return type(x) is type(None)

print('Before:', func(5))
print('After :', func(None))
