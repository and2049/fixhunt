from typing import Optional

def func(x: Optional[int]) -> bool:
    return x is None

print('Before:', func(5))
print('After :', func(None))
