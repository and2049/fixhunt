import trio
async def main():
    """This is a docstring with await trio.sleep(0) inside."""
    s = 'not await trio.sleep(0)'
    # await trio.sleep(0)  # this is a comment
    await trio.sleep(0)  # real call
    print('slept')
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
