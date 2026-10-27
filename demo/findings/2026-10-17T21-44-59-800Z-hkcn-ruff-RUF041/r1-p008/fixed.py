from typing import Literal
x = Literal['a', 'b', 'c']
print(x.__args__)
def side_effect():
    global x
    x = Literal['d']
side_effect()
print(x.__args__)
