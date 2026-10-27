from functools import lru_cache
@lru_cache()
def fmt(x):
  return f'Value: {x!r}'
print(fmt(42))
print(fmt(42))  # cached
