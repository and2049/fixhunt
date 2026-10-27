import sys
module_dict = {'x': 1}
sys.modules[__name__].dict = module_dict
exec('''
from dict import *
if 'x' in dict and dict['x']:
    print('starred access')
''', globals())
