from typing import TypeVar
T = TypeVar('T')
class FakeBool:
    def __init__(self, val): self.val = val
    def __bool__(self): return self.val is not None
    def __eq__(self, other): return isinstance(other, FakeBool) and self.val == other.val
def check(x: T) -> T:
    if x is None:
        return x
    if x:
        return FakeBool(True)
    return x
result = check(FakeBool(0))
print(f"Result truthy: {bool(result)}, Result is FakeBool(True): {result == FakeBool(True)}")
