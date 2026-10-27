def f(pos, /, *, kw=None, **kwargs):
    if pos == 0:
        return
    return

print(f(0))
print(f(1, kw=2, extra=3))
