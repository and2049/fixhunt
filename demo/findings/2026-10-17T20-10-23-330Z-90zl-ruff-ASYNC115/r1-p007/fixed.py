import trio
import trio.lowlevel
# trio.lowlevel not imported
async def main():
    await trio.lowlevel.checkpoint()  # should become trio.lowlevel.checkpoint()
    print('checkpoint passed')
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
