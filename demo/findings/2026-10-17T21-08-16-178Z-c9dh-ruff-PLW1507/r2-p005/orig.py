import copy
import os
state = []
class Track:
    def __init__(self, name):
        self.name = name
    def __copy__(self):
        state.append(f'copied {self.name}')
        return self
    def copy(self):
        state.append(f'.copy {self.name}')
        return self
a = Track('a')
b = Track('b')
result = copy.copy(a) if state.append('eval') or True else b
print('state:', state)
print('result name:', result.name)
