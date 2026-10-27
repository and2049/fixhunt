# -*- coding: utf-8 -*-
class Key:
    def __init__(self, v):
        self.v = v
    def __eq__(self, other):
        return isinstance(other, Key) and self.v == other.v
    def __hash__(self):
        return hash(self.v)
d = {Key(1): 'a', Key(1): 'b'}
print(len(d))
