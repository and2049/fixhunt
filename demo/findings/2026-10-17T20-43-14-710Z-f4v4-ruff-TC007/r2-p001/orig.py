import sys
from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from collections import deque
MyAlias: TypeAlias = \
    deque[int]
def main():
    try:
        x = MyAlias()  # This will fail after fix because MyAlias becomes string
        print('success:', len(x))
    except Exception as e:
        print(type(e).__name__, ':', e)
main()
