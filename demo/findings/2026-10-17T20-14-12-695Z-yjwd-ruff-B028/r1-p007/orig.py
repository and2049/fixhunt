import warnings
import sys
if sys.version_info < (3, 12):
    warnings.warn('test', skip_file_prefixes=['ignore_me'])
    print('skip_file_prefixes used (ignored in <3.12)')
else:
    print('skip_file_prefixes respected')
