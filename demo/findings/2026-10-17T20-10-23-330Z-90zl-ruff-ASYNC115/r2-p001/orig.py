import trio
async def main():
    delay_val = 0
    await trio.sleep(delay=delay_val)
    print('keyword ok')
await trio.run(main())
