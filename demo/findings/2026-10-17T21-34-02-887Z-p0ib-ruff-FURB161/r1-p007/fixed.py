import sys
mod = type('M', (), {})
mod.VALUE = 42
sys.modules['mymod'] = mod
from mymod import *
print(VALUE)
print(bin(VALUE).count('1'))
