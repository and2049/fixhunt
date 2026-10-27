
async def gen():
    yield 'hi'.encode('utf-8')  # UP012 triggers

async def main():
    g = gen()
    first = [x async for x in g]
    try:
        second = [x async for x in g]  # reused generator
    except StopAsyncIteration:
        second = []
    print(f'{len(first)} {len(second)}')

import asyncio
asyncio.run(main())
