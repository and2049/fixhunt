import pathlib
class BoolObj:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        print(f'__bool__ called with {self.val}')
        return bool(self.val)
obj = BoolObj(0)
pathlib.Path('test.txt').write_text('yes' if obj else 'no')
with open('test.txt') as f:
    print(f.read())
import os
os.remove('test.txt')
