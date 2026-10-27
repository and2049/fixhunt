def f(pos, /, kw=None, *args, **kwargs):
    if TYPE_CHECKING:
        pass
print(f(1, kw=2, extra=3))
