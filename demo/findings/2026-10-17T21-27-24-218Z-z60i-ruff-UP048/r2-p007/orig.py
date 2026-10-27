from typing import List
# Use annotation at runtime via __annotations__
def f() -> List[int]:
    while 1:
        return [1]

# Trigger annotation evaluation
print(f.__annotations__['return'])
# Call f to ensure loop ran
print(f())
