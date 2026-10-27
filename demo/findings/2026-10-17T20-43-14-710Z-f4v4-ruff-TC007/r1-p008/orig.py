from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from builtins import str as _str
StrAlias: TypeAlias = _str
str = lambda x: f'[{x}]'  # shadow built-in
print('StrAlias("hi"):', StrAlias('hi'))
# After fix: StrAlias becomes "_str", which is not callable
