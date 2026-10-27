def f(pos, /, kw=None, *args, **kwargs):
    if TYPE_CHECKING:
        pass
    return pos, kw, args, kwargs
print(f(1, kw=2, extra=3))
