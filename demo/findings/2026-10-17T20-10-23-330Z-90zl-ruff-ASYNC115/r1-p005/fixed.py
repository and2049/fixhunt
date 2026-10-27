import trio
import trio.lowlevel
counter = 0
async def inc():
    global counter
    counter += 1
    return counter
async def main():
    global counter
    counter = 0
    results = []
    for i in range(2):
        val = inc()
        await trio.lowlevel.checkpoint()
        results.append((val, counter))
    print('results:', results)
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
