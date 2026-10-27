async def inc(x):
    await asyncio.sleep(0)
    return x + 1

async def main():
    x = 1
    x = await inc(x)
    print('plain await:', x)
    x += 1  # This is not awaitable; if x were a future, would differ
    print('aug after:', x)

import asyncio
asyncio.run(main())
