# -*- coding: utf-8 -*-
from typing import List
class C:
    x: List[int] = []
    def __init__(self):
        self.x.append(len(self.x))
print(C().x)
