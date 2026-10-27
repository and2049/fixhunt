from typing import Set

def make_set(n: int) -> Set[int]:
    s: Set[int] = set()
    for i in range(n):
        s.add(i)
    return s

s1 = make_set(3)
s2 = make_set(2)
print('s1:', sorted(s1))
print('s2:', sorted(s2))
print('intersection:', sorted(s1 & s2))
