import typing
counter = 0
def inc():
    global counter
    counter += 1
    return counter
if typing.TYPE_CHECKING and inc():
    x = 1
else:
    x = 2
print(f'x={x}, counter={counter}')
