from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    class HashableObj:
        def __init__(self, val): self.val = val
        def __hash__(self): return hash(self.val)
        def __eq__(self, other): return isinstance(other, HashableObj) and self.val == other.val
MySetType: TypeAlias = HashableObj
s = {MySetType(1), MySetType(1)}  # Should have size 1
print(len(s))
