import os
from pathlib import Path
# Rule doesn't fire here, but show where str() on int is used in path context
num = 42
p = Path(str(num))  # creates Path('42')
print('Path(str(42)):', p.exists())
# Fix would do Path(42) -> TypeError: expected str, bytes or os.PathLike object, not int
try:
    Path(42)
except TypeError as e:
    print('Path(42) error:', e)
