from typing import List

def f() -> List[int]:
    x = 1
    return [x]  # type: ignore[list-item]

result = f()
print(len(result))
for item in result:
    print(item)
