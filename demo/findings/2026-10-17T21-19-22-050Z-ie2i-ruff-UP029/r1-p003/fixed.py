class A:
    def __hash__(self): return 1
    def __eq__(self, other): return isinstance(other, A)
from builtins import dict
d = {A(): 1, A(): 2}
print(len(d))
