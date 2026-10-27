from typing import List
T = list([int])
def func(x: T[0]) -> None:
    print('Received:', x)
func(42)
