from typing import Literal

x = Literal[Literal['hello'], Literal['world']]
s = '%s %s' % (x.__args__[0][0], x.__args__[1][0])
print(s)
print(f'{x.__args__[0][0]} {x.__args__[1][0]}')
print(str(x))
print(repr(x))
