import functools
@functools.cache
async def fetch(n):
    await __import__('asyncio').sleep(0)
    return n * 2
import asyncio
async def main():
    r1 = await fetch(3)
    r2 = await fetch(3)
    print('Cached async results:', r1, r2)
asyncio.run(main())
