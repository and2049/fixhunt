import sys
mod = type('m', (), {})()
sys.modules['m'] = mod
mod._side = print('module side effect')
# This won't trigger rule, testing isolation
if hasattr(mod, '_side'):
    print('side effect seen')
