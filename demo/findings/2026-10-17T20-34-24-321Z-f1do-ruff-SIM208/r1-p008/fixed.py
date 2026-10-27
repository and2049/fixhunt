import sys
mod = sys.modules[__name__]
if not hasattr(mod, '_init'):
    mod._init = True
    mod.state = 0

def side_effect():
    mod.state += 1
    return mod.state > 0

if side_effect():
    print('state after:', mod.state)
else:
    print('unreachable')
print('final state:', mod.state)
