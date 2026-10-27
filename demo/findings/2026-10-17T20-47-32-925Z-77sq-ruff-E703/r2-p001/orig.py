from __future__ import annotations
T = list
def f(x: T) -> T:
  return x
print(f.__annotations__)  # Shows stringized annotation
f([1]);
