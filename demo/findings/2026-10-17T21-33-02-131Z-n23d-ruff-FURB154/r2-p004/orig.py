async def f():
    global x
    global y
    await asyncio.sleep(0)
    return x + y
x = 1
y = 2
import asyncio
print(asyncio.run(f()))
