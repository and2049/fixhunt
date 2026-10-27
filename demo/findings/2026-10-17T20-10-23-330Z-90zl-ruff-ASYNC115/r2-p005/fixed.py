import trio
async def main():
    await trio.sleep(
        0  # zero delay
    )
    print('comment preserved')
trio.run(main())
