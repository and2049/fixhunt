T = {1, 2}
def f(x: T) -> int:
    return x
try:
    print(f(1))
except Exception as e:
    print(type(e).__name__, e)
