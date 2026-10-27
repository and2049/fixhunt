import trio as t
import anyio as a
import trio.lowlevel
import anyio.lowlevel
async def main():
    await trio.lowlevel.checkpoint()
    await anyio.lowlevel.checkpoint()
    print('both checkpoints passed')
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
