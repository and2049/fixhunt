import os
import tempfile
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, 'link')
    os.symlink('target', p)
    if os.path.exists(p):
        return os.readlink(p)
print('no return')
