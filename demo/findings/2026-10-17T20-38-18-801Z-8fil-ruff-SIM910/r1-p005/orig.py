import os
from pathlib import Path
cache = {}
def check_path(p):
    if p not in cache:
        cache[p] = Path(p).exists()
    return cache.get(p, None)

print(check_path('nonexistent.txt'))
print(check_path('nonexistent.txt'))  # Should be cached
