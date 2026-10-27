from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nonexistent import something  # This import is only for type checking

x = None
if type(x) is type(None):
    print('x is None')
else:
    print('x is not None')
