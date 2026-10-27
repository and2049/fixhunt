import functools
funcs = []
for i in range(2):
    if (n := i) == 0:
        @functools.lru_cache(maxsize=None)
        def g(x): return x + n
        funcs.append(g)
print('Results:', [f(5) for f in funcs])  # Should differ if timing/scoping broken by rewrite
