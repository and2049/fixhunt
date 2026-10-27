from typing import Literal

LIT = Literal[Literal['init']]

class C:
    attr = LIT  # Evaluated at class definition time
    def __init__(self):
        self.val = self.attr

print(C().val)
