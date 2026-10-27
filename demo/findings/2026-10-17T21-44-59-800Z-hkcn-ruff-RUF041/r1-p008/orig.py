from typing import Literal
x = Literal[Literal['a', 'b'], Literal['c']]
print(x.__args__)
def side_effect():
    global x
    x = Literal['d']
side_effect()
print(x.__args__)
