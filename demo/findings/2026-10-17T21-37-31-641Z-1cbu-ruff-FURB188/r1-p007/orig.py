from typing import List
s: str = 'prefix'
p: str = 'pre'
if s.startswith(p):
    s = s[:-len(p)] if s.startswith(p) else s
print(s)
