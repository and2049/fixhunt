import functools
@functools.lru_cache()
def fmt_cached(x):
    s = str(x)
    return f'{repr(s)} | {s!r} | %{s}
'
print(fmt_cached('hello\	world'))
print(fmt_cached(42))
# Second call should hit cache
print(fmt_cached('hello\	world'))
