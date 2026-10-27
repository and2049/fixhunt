__all__ = ['helper']
def helper(x):
    return x * 2
from helper_mod import *  # Simulate via exec
exec('''
def helper(x):
    return x + 1
''', globals(), locals())
a, b, c = 1, 2, 3
if a < b < c:
    print(helper(10))
# Cleanup
if 'helper_mod' in locals():
    del helper_mod
