import tempfile
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('a\nb\nc')
    fname = f.name
with open(fname, 'r') as f:
    lines = f.readlines()
sorted_lines = sorted(lines)
print('Sorted lines:', [repr(l) for l in sorted_lines])
import os
os.unlink(fname)
