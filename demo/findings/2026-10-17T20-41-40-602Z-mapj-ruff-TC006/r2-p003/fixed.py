from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from typing import List
    MyType = List[int]
x = 5
y = typing.cast("MyType", [x])  # Rule triggers: MyType is not a string
print(sum(y))
