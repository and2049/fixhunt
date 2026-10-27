from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    X = 42
Y: TypeAlias = X  # value from TYPE_CHECKING
print('Y equals:', Y)
# After fix: Y: TypeAlias = "X  # value from TYPE_CHECKING" becomes invalid or misparsed
