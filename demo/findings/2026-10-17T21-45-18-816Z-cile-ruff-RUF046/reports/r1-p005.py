import inspect
src = inspect.getsource(lambda: int(5 + 3))
print('Source length of int(5+3):', len(src.strip()))
