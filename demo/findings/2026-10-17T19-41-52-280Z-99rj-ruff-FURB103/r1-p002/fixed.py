from typing import List
import pathlib
T = int
def get_data() -> T:
    return 42
pathlib.Path('out.txt').write_text(str(get_data()))
with open('out.txt') as f:
    print(f.read())
import os
os.remove('out.txt')
