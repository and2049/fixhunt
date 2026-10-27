class MyGen:
    def __bool__(self): return False
    def __len__(self): return 0
def f() -> Generator[MyGen, None, None]:
    yield MyGen()
g = f()
print(bool(g))
print(g is None)
