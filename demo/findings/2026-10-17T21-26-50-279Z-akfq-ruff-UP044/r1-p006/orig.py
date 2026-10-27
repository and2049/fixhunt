from typing import Unpack
vals = [1, 2]
f = lambda *args: (n := len(args)) + sum(args)
print(f(*vals))
print('n leaked?', 'n' in locals())
