import functools
decorator = '@functools.lru_cache()'
exec(decorator + '
def f(): return 1')
print(f())
