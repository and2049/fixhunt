async def f():
    return 1

async def main():
    r = await f()
    if r == 1 or r == 2:
        print('yes')
    else:
        print('no')
import asyncio
asyncio.run(main())
