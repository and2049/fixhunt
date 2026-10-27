import typing
t = typing.get_type_hints(lambda: None).__annotations__
def f() -> Generator[int, None, None]: pass
t2 = typing.get_type_hints(f).__annotations__['return']
print(str(t2))
