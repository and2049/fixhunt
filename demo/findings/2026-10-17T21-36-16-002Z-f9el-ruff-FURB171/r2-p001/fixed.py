from typing import List

def f() -> List[int]:
    return []

x = 1
if x in [f()[0]] if f() else [0]:  # Rule fires on [0]
    print('in')
else:
    print('not in')
