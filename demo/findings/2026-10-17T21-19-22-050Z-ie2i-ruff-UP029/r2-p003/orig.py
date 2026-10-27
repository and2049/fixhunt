class DummyModule:
    builtins = 'shadow'

import sys
sys.modules['dummy'] = DummyModule()

from dummy import builtins
print(builtins)
