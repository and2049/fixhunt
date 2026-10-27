import sys
mod = type('m', (), {})()
mod.state = 0
sys.modules['testmod'] = mod
exec("""
state = 0
def func():
    global state
    state += 1
    return state > 0
""", mod.__dict__)
from testmod import *
if func() and not func():
    pass
print('testmod.state:', mod.state)
