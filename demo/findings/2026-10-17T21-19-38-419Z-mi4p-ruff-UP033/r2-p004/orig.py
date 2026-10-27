import functools
from typing import List, Optional

@functools.lru_cache(maxsize=None)
def process_data(items: List[int]) -> Optional[int]:
    if not items:
        return None
    return sum(items)

# Trigger annotation evaluation at runtime
print(process_data.__annotations__)
result = process_data([1, 2, 3])
print(result)
print(process_data([1, 2, 3]))  # Cached
