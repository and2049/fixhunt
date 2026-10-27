from typing import Literal
int = lambda: print('custom_int')
x = Literal['a', 'b']
print(int(), getattr(x, '__args__', x))
del int
int = 42
try:
    print(int)
except Exception as e:
    print(type(e).__name__, str(e))
