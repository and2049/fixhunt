async def async_gen():
    yield 1
    yield 2
async def main():
    ag = async_gen()
    x = await ag.__anext__()
    vals = []
    async for v in ag:
        if x == v or x == v:
            vals.append(v)
    print('Vals:', vals)
asyncio.run(main())
import asyncio
