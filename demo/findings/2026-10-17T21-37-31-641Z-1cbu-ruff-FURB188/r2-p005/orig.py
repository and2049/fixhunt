from __future__ import annotations
prefix: str = 'xyz'
s: str = 'xyz123'
if s.startswith(prefix):
    s = s[len(prefix):]
print(s)
