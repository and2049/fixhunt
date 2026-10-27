from typing import List
x: List[int] = [] if [] else [1]
print('ternary:', x)
# After fix: x = [] or [1]
x = [] or [1]
print('or     :', x)
