from __future__ import annotations
class A:
    x = 1
    def __init__(self):
        self.y = self.x
    @property
    def z(self):
        return self.y + 1
print(A().z)
