from typing import TypeAlias
BadAlias: TypeAlias = "int" "|" "None"
print(repr(BadAlias))
