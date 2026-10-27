async def gen():
    yield 1
    raise (ValueError('async'))()

async def main():
    try:
        async for x in gen():
            print('Yielded:', x)
    except ValueError as e:
        print('Caught async:', e.args[0])

import asyncio
asyncio.run(main())
