from typing import List
x: List[int] = [1, 2, 3]
if 2 in [1, 2, 3]:
    print('Found 2 in list')
if 2 in {1, 2, 3}:
    print('Found 2 in set')
