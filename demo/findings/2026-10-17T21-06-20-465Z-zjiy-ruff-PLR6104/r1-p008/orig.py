import os
os.symlink('tmp', 'link')
with open('tmp', 'w') as f: f.write('hi')
from pathlib import Path
p = Path('link')
p = p + '/../tmp'  # Trigger: Path doesn't support + with str -> TypeError
# Fix: use / operator
p = Path('link')
p = p / '../tmp'   # Trigger
print(p.exists())
# After fix: p /= '../tmp' -> same
# But if we override __truediv__? No.
# Instead: make wrapper that logs
class P:
    def __init__(self, s): self.s = s
    def __truediv__(self, other): return P(self.s + '/' + other)
    def __itruediv__(self, other): self.s = self.s + '/' + other; return self
    def exists(self): return os.path.exists(self.s)
p = P('link')
p = p / '../tmp'  # Trigger
print(p.exists())
# After: p /= '../tmp' -> mutates self.s in place
