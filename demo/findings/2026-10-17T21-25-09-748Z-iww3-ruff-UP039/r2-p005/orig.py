class B() -> str:
    return 'test'

print(B.__annotations__)
try:
    B()
except TypeError as e:
    print(f'{type(e).__name__}: {e}')
del B
