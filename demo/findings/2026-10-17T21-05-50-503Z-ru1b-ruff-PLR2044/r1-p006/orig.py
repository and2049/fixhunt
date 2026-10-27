from testmod import *  # 
print(__all__ if '__all__' in globals() else 'no __all__')
# Cleanup
try:
    del testmod
    del __all__
except:
    pass
# Recreate module state
import sys
if 'testmod' in sys.modules:
    del sys.modules['testmod']
exec("
class testmod:
    __all__ = ['A']
    A = 5
sys.modules['testmod'] = testmod
", globals(), locals())
from testmod import *  # real comment
print(__all__ if '__all__' in globals() else 'no __all__')
print(A)
