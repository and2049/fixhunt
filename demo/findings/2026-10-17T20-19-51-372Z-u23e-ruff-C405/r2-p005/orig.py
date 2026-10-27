async def gen():
    yield 1
    yield 2
async def main():
    g = gen()
    lst = [x async for x in g]
    s = set(lst)
    print(f'Set from async gen: {s}')
import asyncio
asyncio.run(main())
