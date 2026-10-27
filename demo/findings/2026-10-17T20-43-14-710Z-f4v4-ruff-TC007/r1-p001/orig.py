from typing import TYPE_CHECKING, TypeAlias
import sys
if TYPE_CHECKING:
    from collections import UserList
class UserList(UserList):
    pass
DEFAULT_VAL: TypeAlias = UserList
@no_type_check
def func(a, *, b=DEFAULT_VAL()):
    return len(b)
try:
    print(func(1))
except Exception as e:
    print(type(e).__name__, e)
func.__defaults__ = (None,)  # reset for second call
print(func(2))
