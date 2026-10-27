from typing import TypeVar
T = TypeVar('T')
class Buffer:
    def __init__(self): self.data = []
    def write(self, x): self.data.append(x)
    def __enter__(self): return self
    # Note: no __exit__ or close!
def process(x: T) -> T:
    with Buffer() as b:
        b.write(x)
    return x
result = process("hello")
print(f"Buffer data: {result}")
