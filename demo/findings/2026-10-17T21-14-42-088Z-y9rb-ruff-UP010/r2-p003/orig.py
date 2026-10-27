from __future__ import annotations
f = []
for i in range(2):
    if (x := i) not in f:
        f.append(x)
        f.append(lambda: x)
print([g() for g in f[2:]])
