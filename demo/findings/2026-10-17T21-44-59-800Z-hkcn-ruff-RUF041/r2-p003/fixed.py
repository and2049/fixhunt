from typing import Literal

# Comment before
x = Literal[
    Literal['a'  # inline comment for a
    ],
    Literal['b']  # inline comment for b
]
print(x.__args__)
