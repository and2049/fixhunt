async def gen():
    obj = type('Obj', (), {'value': 42})()
    yield obj.value

async def main():
    async for x in gen():
        print(x)

import asyncio
asyncio.run(main())
