from typing import Literal
async def gen():
    yield 1
    await gen()
async def main():
    x = Literal[Literal[gen()], Literal[2]]
    async for v in gen():
        print(v, x.__args__)
import asyncio
asyncio.run(main())
