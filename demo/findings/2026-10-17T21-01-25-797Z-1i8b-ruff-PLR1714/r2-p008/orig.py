import os
import pathlib
os.symlink('tmp', 'link')
try:
    p = pathlib.Path('link')
    o = os.path
    if p.exists() or o.exists('link'):
        print('exists')
    else:
        print('missing')
except Exception as e:
    print(type(e).__name__, e)
finally:
    try: os.unlink('link')
    except: pass
