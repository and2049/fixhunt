from pathlib import Path
import os
os.symlink('target', 'link')
p = Path('link')
try:
    if p.exists() and p.exists():
        print('both true')
    else:
        print('at least one false')
except Exception as e:
    print(type(e).__name__, e)
finally:
    try:
        os.unlink('link')
    except:
        pass
