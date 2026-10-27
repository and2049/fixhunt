async def gen():
    yield 1
    await asyncio.sleep(0)
    yield 2

async def main():
    g = gen()
    first = await g.__anext__()
    # Rule fires on: second if not first else 0
    second = first if not first else 0  # not first -> False, so second=first
    print(f'first={first}, second={second}')
    try:
        await g.__anext__()
    except StopAsyncIteration:
        print('done')

import asyncio
asyncio.run(main())
