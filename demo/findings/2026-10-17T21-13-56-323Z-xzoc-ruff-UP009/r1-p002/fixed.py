async def gen():
    yield 1
    await asyncio.sleep(0)
async def main():
    g = gen()
    print(await g.__anext__())
import asyncio
asyncio.run(main())
