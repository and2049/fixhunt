import typing
class Ctx:
    def __enter__(self):
        return 42
    def __exit__(self, *exc):
        pass
def f():
    with Ctx() as c:
        x = typing.cast("list[int]", [c])
        return sum(x)
print(f())
