from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    class _Tmp: pass

class B(object):
    attr: 'List[int]' = [1, 2, 3]
    def method(self) -> int:
        return len(self.attr)

b = B()
print(b.method())
