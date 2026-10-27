async def gen(l):
    yield l
    l = l[::-1]
    yield l

async def main():
    l = [1, 2, 3]
    g = gen(l)
    print('first:', await g.__anext__())
    print('second:', await g.__anext__())

import asyncio
asyncio.run(main())
