from typing import TypeAlias
ListInt: TypeAlias = "list[int]"
def f(x=ListInt()):
    x.append(1)
    return x
print(f())
print(f())
