import os
import tempfile
with tempfile.TemporaryDirectory() as td:
    p = os.path.join(td, 'link')
    class P:
        def __contains__(self, k): return os.path.exists(p) if k == 'x' else False
        def __getitem__(self, k):
            raise KeyError(k)
    d = P()
    if "x" in d and d["x"]:
        print("falsy")
