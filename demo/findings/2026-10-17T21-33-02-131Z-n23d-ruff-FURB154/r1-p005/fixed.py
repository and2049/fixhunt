async def f():
    global x, y
    x = 1
    await asyncio.sleep(0)
    y = 2
    yield x + y
import asyncio
async def main():
    gen = f()
    val = await gen.__anext__()
    print('value:', val)
    print('x=', x, 'y=', y)
asyncio.run(main())
