from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    IntVal = int
Stored: TypeAlias = IntVal
class IntDescriptor:
    def __init__(self, value: Stored) -> None:
        self.value = value
    def __get__(self, instance, owner):
        return self.value if instance is None else instance._val
class A:
    x = IntDescriptor(5)
print('Descriptor value:', A().x)
