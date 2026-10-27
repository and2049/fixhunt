def gen():
    try:
        yield 1
        raise ValueError('bad')
    finally:
        print("finally executed")

try:
    s = set(x for x in gen())
except ValueError as e:
    print(f"Caught: {type(e).__name__}: {e}")
