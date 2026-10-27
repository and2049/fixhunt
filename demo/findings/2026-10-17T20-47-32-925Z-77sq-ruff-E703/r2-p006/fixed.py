import os
import pathlib
open('tmp.txt', 'w').write('hi')
os.symlink('tmp.txt', 'link')
print(os.path.exists('link'))  # Semicolon on import os line
print(pathlib.Path('link').exists())
os.unlink('link'); os.remove('tmp.txt')
