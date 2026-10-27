from typing import List
T = List[int]
def f() -> T:
  x = [1, 2]
  if x:
    return x.pop()
print(f(), f())
