open = lambda *a, **k: (_ for _ in ()).throw(ValueError('bad'))
txt = b'hi'
with open('t.bin', 'wb') as f:
    f.write(txt)
del open
with open('t.bin', 'wb') as f:
    f.write(txt)
with open('t.bin', 'rb') as f:
    print(f.read())
import os
if os.path.exists('t.bin'):
    os.remove('t.bin')
