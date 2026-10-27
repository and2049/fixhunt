from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    MyInt = int
Number: TypeAlias = MyInt
print('Alias repr:', repr(Number))
print('Alias str:', str(Number))
# Expected: <class 'int'> or similar; after fix: "MyInt"
