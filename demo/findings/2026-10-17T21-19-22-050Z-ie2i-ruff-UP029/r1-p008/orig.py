class X:
    def __bool__(self): return False
    def __len__(self): return 0
from builtins import bool
b = bool(X())
print(b, b is False, b == False)
