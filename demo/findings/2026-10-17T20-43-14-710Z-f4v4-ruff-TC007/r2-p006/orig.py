from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    def factory() -> int:
        raise ValueError('bad')
AliasFactory: TypeAlias = factory()
try:
    x = AliasFactory  # After fix: x is string "factory()", no call → no exception
    print('value:', x)
except ValueError as e:
    print('caught:', e)
else:
    print('no exception')
finally:
    print('finally')
