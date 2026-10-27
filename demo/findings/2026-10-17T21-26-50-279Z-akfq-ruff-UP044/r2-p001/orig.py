from typing import Unpack
n = 3
data = [(i,) for i in range(n)]
fns = [lambda *x=*t: sum(x) for t in data]
print([f() for f in fns])
