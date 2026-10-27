from typing import List
s: List[int] = [1, 2]
try:
    for x in s:
        s.append(3)
except NameError as e:
    print('NameError:', type(e).__name__, str(e))
print('s:', s)
