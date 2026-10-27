import os
from pathlib import Path
p = 'tmp'  # noqa: FAKE
os.mkdir(p)
os.symlink('tmp/target', p + '/link')
print(Path(p + '/link').resolve() == Path(os.path.realpath(p + '/link')))
