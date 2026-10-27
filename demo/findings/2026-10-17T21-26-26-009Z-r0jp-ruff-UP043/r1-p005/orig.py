from types import NoneType as None
def f() -> Generator[int, None, None]:
    yield 1
gen = f()
print(next(gen))
