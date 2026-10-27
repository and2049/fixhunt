from typing import List
try:
    [1, 2] + 'a'
except (TypeError,):
    print('type error')
