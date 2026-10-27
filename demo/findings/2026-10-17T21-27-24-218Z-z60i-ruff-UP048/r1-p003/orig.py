async def gen():
    i = 0
    while 1:
        if i >= 2:
            break
        yield i
        i += 1

async def main():
    res = []
    async for x in gen():
        res.append(x)
    print(res)

import asyncio
asyncio.run(main())
