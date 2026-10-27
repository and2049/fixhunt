# Simulate a module with side effects on import
import sys
if 'hazard_mod' not in sys.modules:
    exec("""
# hazard_mod.py
_side_effect = []
def register(x):
    _side_effect.append(x)
    return x
__all__ = ['register']
""", {'__name__': 'hazard_mod'})
    sys.modules['hazard_mod'] = sys.modules.get('hazard_mod', type('hazard_mod', (), {}))
    hazard_mod = sys.modules['hazard_mod']
    hazard_mod._side_effect = []
    hazard_mod.register = lambda x: (hazard_mod._side_effect.append(x), x)[1]
    hazard_mod.__all__ = ['register']

from hazard_mod import *  # star-import

lists = [[1], [2], [3]]
print('Before sum:', hazard_mod._side_effect)
result = sum(lists, [])
print('After sum:', hazard_mod._side_effect)
print('Result:', result)
