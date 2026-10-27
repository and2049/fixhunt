from typing import List, Optional

def f(x: Optional[int]) -> List[int]:
    if x is None:
        return None
    return [x] * 2

print(f(None))
print(f(3))
