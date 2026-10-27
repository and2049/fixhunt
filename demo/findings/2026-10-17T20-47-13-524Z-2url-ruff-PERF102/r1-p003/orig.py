from typing import List
def f() -> List[int]:
    d = {1: 10}
    for k, _ in d.items():
        return [k]
print(f())
