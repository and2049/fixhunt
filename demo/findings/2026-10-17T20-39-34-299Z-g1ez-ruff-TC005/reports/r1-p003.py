def f(a=None):
    if a is None:
        a = []
    if TYPE_CHECKING:
        pass
print(f())
