import sys
counter = [0]
orig_import = __import__
def side_effect_import(name, *args, **kwargs):
    if name == 'sys':
        counter[0] += 1
    return orig_import(name, *args, **kwargs)

# Temporarily replace __import__ to observe side effects
builtins = __import__('builtins')
builtins.__import__ = side_effect_import
try:
    v = int(__import__('sys').maxsize)
    print('sys imported', counter[0], 'times')
    print('value:', v)
except Exception as e:
    print('error:', type(e).__name__, str(e))
finally:
    builtins.__import__ = orig_import
