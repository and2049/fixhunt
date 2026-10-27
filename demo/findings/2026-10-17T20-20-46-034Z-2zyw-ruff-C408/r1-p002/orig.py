async def gen():
    yield await list().__repr__()
async def main():
    g = gen()
    print(await g.__anext__())
import asyncio
asyncio.run(main())
