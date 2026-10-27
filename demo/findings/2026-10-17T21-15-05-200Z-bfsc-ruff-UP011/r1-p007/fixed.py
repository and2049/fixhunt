def outer():
  lru_cache = lambda f: f  # breaks lru_cache
  from functools import lru_cache as real_lru
  @real_lru
  def inner():
    return 1
  return inner()
print(outer())
