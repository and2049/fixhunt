import os
import tempfile
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, 'test.txt')
    open(p, 'w').write('hello')
    print(os.path.exists(p))
    from pathlib import Path
    print(Path(p).exists())
