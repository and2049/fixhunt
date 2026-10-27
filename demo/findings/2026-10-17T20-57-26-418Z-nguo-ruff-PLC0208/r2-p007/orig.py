import os
from pathlib import Path
for p in {Path('a'), Path('b')}:
    p.write_text(p.name)
    print(p.read_text().strip())
for p in {Path('a'), Path('b')}:
    p.unlink()
