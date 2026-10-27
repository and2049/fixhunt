class SlotClass:
    __slots__ = ["x", "y"]
    x: int = 0
    y: int = 0

obj = SlotClass()
obj.x = 1
obj.y = 2
print(f'x={obj.x}, y={obj.y}')
