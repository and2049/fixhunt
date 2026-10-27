async def g():
    return []

async def main():
    x = await g()
    print(type(x))

import asyncio
asyncio.run(main())
