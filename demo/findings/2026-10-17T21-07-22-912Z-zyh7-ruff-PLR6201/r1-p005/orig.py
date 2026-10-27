import sys
mod = sys
allowed = ['stdout', 'stderr']
if hasattr(mod, 'stdout') and 'stdout' in allowed:
    print('stdout access allowed')
if hasattr(mod, 'stdout') and 'stdout' in {'stdout', 'stderr'}:
    print('stdout access allowed (set)')
