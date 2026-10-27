import tempfile
import os
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('print(__name__, sep=\\'\\'\')
')
    fname = f.name
try:
    exec(open(fname).read(), {'__name__': '__main__'})
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    os.unlink(fname)
