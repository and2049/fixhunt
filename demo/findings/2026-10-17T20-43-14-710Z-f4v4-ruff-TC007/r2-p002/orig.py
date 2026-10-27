from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    class A: ...
MyType: TypeAlias = A
obj = object()
print(isinstance(obj, MyType))  # Before: False, After: TypeError (str vs type)
