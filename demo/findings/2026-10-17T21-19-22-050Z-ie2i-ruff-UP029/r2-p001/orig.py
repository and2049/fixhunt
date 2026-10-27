from typing import List
from builtins import str

def f(x: 'List[str]') -> None:
    print(len(x))

f(['a', 'b'])
