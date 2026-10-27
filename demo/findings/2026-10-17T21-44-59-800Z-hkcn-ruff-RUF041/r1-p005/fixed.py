from typing import Literal, get_args
x = Literal['a', 'b', 'c']
args = get_args(x)
print(len(args), [get_args(a) if hasattr(a, '__args__') else a for a in args])
