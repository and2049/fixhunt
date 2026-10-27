import os
from pathlib import Path
p = Path('tmp')
p.write_text('test')
try:
    if str(p) == 'tmp' or os.fsencode(p) == b'tmp':
        print('path matched')
    else:
        print('no match')
except Exception as e:
    print(type(e).__name__, e)
finally:
    p.unlink(missing_ok=True)
