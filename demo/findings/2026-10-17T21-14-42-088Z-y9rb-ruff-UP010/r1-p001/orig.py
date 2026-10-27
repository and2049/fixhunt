# This import triggers evaluation of __future__ annotations, which creates _Feature object
from __future__ import annotations

# Variable exists only because the import caused __future__ module to be loaded
# and we access a side-effect attribute
try:
    x = __import__('__future__').annotations._Feature.value
    print(f'x = {x}')
except AttributeError as e:
    print(f'AttributeError: {e}')
