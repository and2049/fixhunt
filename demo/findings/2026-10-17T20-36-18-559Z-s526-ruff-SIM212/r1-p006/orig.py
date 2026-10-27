import sys
sys.modules[__name__]._side = []

def _init():
    sys.modules[__name__]._side.append('loaded')

_init()
from __main__ import *  # triggers side effect via _init

# Rule fires: msg if not loaded else 'default'
loaded = len(sys.modules[__name__]._side) > 0
msg = 'hello'
result = msg if not loaded else 'default'
print(f'loaded={loaded}, result={result}, side={sys.modules[__name__]._side}')
