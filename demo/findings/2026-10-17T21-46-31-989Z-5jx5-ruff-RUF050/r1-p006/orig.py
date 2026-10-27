async def gen():
    if False:
        yield 1
    return 2
import asyncio
print(asyncio.run(gen()))
