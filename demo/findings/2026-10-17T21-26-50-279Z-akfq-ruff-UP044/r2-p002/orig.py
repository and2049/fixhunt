from typing import Unpack
def f(x: Unpack[ # comment
    tuple[int, str]]) -> None:
    pass
f((1, 2))
print('ok')
