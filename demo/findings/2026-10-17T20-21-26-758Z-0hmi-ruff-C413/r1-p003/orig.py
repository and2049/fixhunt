import sys
mod = sys.modules['__main__']
mod.COUNTER = 0
class Dummy:
    def __init__(self):
        mod.COUNTER += 1
    def __lt__(self, other):
        return True
from __main__ import *
data = [Dummy(), Dummy()]
sorted_data = sorted(data)
list_wrapped = list(sorted_data)
print('COUNTER after list(sorted):', mod.COUNTER)
print('Length:', len(list_wrapped))
