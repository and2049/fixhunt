import trio
async def main():
    sleep_fn = getattr(trio, 'sleep')
    await sleep_fn(0)
    print('getattr ok')
trio.run(main())
