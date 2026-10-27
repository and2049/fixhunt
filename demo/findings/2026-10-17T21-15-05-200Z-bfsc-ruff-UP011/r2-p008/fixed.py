import sys, os
sys.path.insert(0, os.path.dirname(__file__))
try:
    from .local_functools import lru_cache  # Relative import simulation
    @lru_cache()
    def cached_local(x):
        return x + 10
except ImportError:
    # Fallback: simulate namespace package by importing via package-like name
    import functools as local_functools
    @local_functools.lru_cache
    def cached_local(x):
        return x + 10
print(cached_local(5))
print(cached_local(5))  # Cache hit
# Cleanup
if 'local_functools' in locals():
    del local_functools
if '.' in sys.path[0]:
    sys.path.pop(0)
