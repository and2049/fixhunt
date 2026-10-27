from typing import Literal

x = Literal[
    Literal['a'],  # first
    Literal['b'],  # second
    Literal['c']   # third
]
print([arg for sub in x.__args__ for arg in sub.__args__])
