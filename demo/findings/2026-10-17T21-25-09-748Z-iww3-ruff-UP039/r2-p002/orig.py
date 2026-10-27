__all__ = ['flag']
flag = 0

class Y():
    global flag
    flag += 1

from __main__ import *
print(flag)
