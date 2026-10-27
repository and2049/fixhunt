from typing import TYPE_CHECKING, TypeAlias
"""Module docstring."""
if TYPE_CHECKING:
    from math import pi
    TWO_PI: TypeAlias = 2 * pi  # constant
print('Constant value:', TWO_PI)
# After fix: the inline comment may be wrapped inside quotes, becoming part of the string
