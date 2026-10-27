from typing import TYPE_CHECKING, Generator
if TYPE_CHECKING:
    x: Generator[int, None, None]
else:
    x = (i for i in range(3))
print(type(x).__name__)
