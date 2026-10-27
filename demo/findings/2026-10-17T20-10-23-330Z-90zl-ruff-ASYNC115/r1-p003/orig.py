import trio as t
import anyio as a
async def main():
    await t.sleep(0)
    await a.sleep(0)
    print('both checkpoints passed')
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
