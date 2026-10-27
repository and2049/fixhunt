from typing import TypeAlias
from pathlib import Path
P: TypeAlias = "Path"
p: P = Path('.')
print(p.exists())
print(p.is_absolute())
