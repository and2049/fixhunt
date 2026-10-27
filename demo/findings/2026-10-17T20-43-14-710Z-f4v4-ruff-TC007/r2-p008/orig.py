from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    val = 42
AliasFString: TypeAlias = f"value: {val}"
print(AliasFString)  # Before: 'value: 42', After: 'f"value: {val}"' (literal string)
