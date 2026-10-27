import os
import pathlib
p = pathlib.Path('.')
print('pathlib exists:', p.exists())
print('os.path exists:', os.path.exists('.'))
