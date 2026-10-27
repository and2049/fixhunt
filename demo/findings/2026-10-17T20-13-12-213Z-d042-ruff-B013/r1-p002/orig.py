import os
from pathlib import Path

Path('tmp').mkdir(exist_ok=True)
os.symlink('target', 'tmp/link')

try:
    st = os.lstat('tmp/link')  # Follows symlink by default? No, lstat doesn't.
except (FileNotFoundError,) as e:
    print('os.lstat caught:', type(e).__name__)

try:
    p = Path('tmp/link')
    p.stat()  # Follows symlink
except (FileNotFoundError,) as e:
    print('Path.stat caught:', type(e).__name__)

# Cleanup
os.unlink('tmp/link')
os.rmdir('tmp')
