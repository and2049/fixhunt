from typing import Literal
counter = 0
def inc():
    global counter
    counter += 1
    return counter
class C:
    x = Literal[Literal[inc()], Literal[inc()]]
    y = counter
print(C.x.__args__, C.y)
