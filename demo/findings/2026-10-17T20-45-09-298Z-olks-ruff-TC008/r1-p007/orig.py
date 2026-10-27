from typing import TypeAlias
ListInt: TypeAlias = "list[int]"
s = f"{ListInt}"
print(s)
try:
    eval(s)
except Exception as e:
    print(type(e).__name__, e)
