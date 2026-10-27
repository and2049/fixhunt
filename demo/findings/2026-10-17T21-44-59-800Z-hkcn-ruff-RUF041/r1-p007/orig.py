from typing import Literal, Final, ClassVar
NESTED = Literal[Literal['x'], Literal['y']]
FLAT: Final = Literal['x', 'y']
CLASS_VAR: ClassVar = Literal['x', 'y']
print(NESTED.__args__, FLAT.__args__, CLASS_VAR.__args__)
