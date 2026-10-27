import os
from pathlib import *
import pathlib
def main():
    __all__ = ['p']
    p = lambda x: None
    txt = b'data'
    for name in __all__:
        if name == 'p':
            continue
        try:
            pathlib.Path('tmp.bin').write_bytes(txt)
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
