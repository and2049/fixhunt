from decimal import Decimal
from typing import get_type_hints
def func() -> Decimal:
    return Decimal(1.0 + 2.0)
hints = get_type_hints(func)
print(f'Return type hint: {hints.get("return")}')
val = func()
print(f'Returned value: {val}')
