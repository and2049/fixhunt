import os
import pathlib
if os.path.exists('missing.txt'):
    os.remove('missing.txt')
try:
    pathlib.Path('missing.txt').write_text('should not happen')
except FileNotFoundError as e:
    print(f'Caught: {e}')
print('Done')
