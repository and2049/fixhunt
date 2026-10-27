import typing
T = int
def f(x: 'T') -> None:
    val = not x != 5
    print('val:', val)
f(5)
