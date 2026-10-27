# Simulate .pyi file behavior: type checker expects @functools.lru_cache()
# But we are in .py file - rule will remove parentheses
import functools
@functools.lru_cache
def stubbed_func(x: int) -> str:
    return str(x * 2)
# If type checker sees @functools.lru_cache (no parens) in .pyi, it may error
# We simulate by checking if the decorator form affects runtime
print('Result:', stubbed_func(21))
print('Cached:', stubbed_func.__wrapped__(21) if hasattr(stubbed_func, '__wrapped__') else 'no wrapper')
