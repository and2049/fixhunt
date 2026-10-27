import sys
if 'six' not in sys.modules:
    print('six not loaded')
from six.moves import range
print('six loaded')
