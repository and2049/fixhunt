from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from typing import List
AliasIntList: TypeAlias = List[int]
x: AliasIntList = [1, 2]
print(len(x))  # Should print 2; if misinterpreted, type checker may complain
