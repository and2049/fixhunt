from typing import TypeVar
T_co = TypeVar('T_co', covariant=True)
class Container(Generic[T_co]):
    def __init__(self, item): self.item = item
    @property
    def value(self) -> T_co:
        return self.item
c: Container[object] = Container("str")
print(f"Is str-subtype of object? {isinstance(c.value, str)}")
