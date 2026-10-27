import os
from pathlib import *
def main():
    __all__ = ['p']
    p = lambda x: None
    txt = b'data'
    for name in __all__:
        if name == 'p':
            continue
        try:
            with open('tmp.bin', 'wb') as f:
                f.write(txt)
            break
        except TypeError as e:
            print(e)
    try:
        v = Path('tmp.bin').read_bytes()
        print(v)
    except Exception as e:
        print(type(e).__name__, e)
    finally:
        if os.path.exists('tmp.bin'):
            os.remove('tmp.bin')
main()
