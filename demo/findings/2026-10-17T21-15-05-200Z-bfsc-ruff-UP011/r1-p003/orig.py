from functools import lru_cache
@lru_cache()
def make_adder(n):
  return lambda x: x + n
f1 = make_adder(10)
print(f1(5))
# After fix: same behavior but tests sensitivity
