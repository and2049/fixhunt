import os
import tempfile
with tempfile.TemporaryDirectory() as td:
    p = os.path.join(td, 'link')
    os.symlink('nonexistent', p)
    class P:
        def __contains__(self, k): return os.path.exists(p) if k == 'x' else False
        def __getitem__(self, k):
            if k == 'x': return p
            raise KeyError(k)
    d = P()
    if d.get("x"):
        print("truthy")
    else:
        print("falsy")
