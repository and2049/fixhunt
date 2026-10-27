from typing import TYPE_CHECKING, TypeAlias
def outer():
    if TYPE_CHECKING:
        class Inner: ...
    LocalAlias: TypeAlias = Inner  # Rule should fire here
    try:
        x = LocalAlias()  # Fails after fix: LocalAlias is string
        print('created')
    except Exception as e:
        print(type(e).__name__, ':', e)
outer()
