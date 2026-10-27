from typing import Literal

def gen():
    for item in Literal[Literal['a'], Literal['b']]:
        yield item

g = gen()
print(list(g))  # First consumption
print(list(g))  # Second consumption (should be empty)
