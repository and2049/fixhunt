import tempfile
import os
mod = tempfile.mkstemp()[1]
with open(mod, 'w') as f:
    f.write('x = 42\n__all__ = [\"x\"]')
os.close(int(mod.split(',')[0][1:])) if ',' in mod else os.close(int(mod))
# Simulate import via exec
ns = {}
with open(mod, 'r') as f:
    exec(f.read(), ns)
def h():
    if True:
        return ns['x']
print(h())
os.remove(mod)
