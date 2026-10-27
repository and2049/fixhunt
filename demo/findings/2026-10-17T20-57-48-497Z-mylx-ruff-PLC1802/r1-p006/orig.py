import os
try:
  os.mkdir('tmpdir')
except FileExistsError:
  pass
try:
  os.symlink('tmpdir', 'link')
except FileExistsError:
  pass
p = os.path.exists('link')
print(p)
import shutil
shutil.rmtree('tmpdir', ignore_errors=True)
os.unlink('link')
