from typing import Literal
# This comment should stay after rewrite
x = Literal[
    Literal['hello'],  # inline comment
    Literal['world']
]  # trailing comment
print(x.__args__)
# Another comment to ensure attachment matters
