from typing import TypeVar
T = TypeVar('T')
import functools
@functools.lru_cache(maxsize=128)
def cached_func(x: T) -> T:
    return x
print(cached_func(42))
